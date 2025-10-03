# -*- coding: utf-8 -*-
"""Email adresi doğrulama ve analiz (çekirdek)."""
from typing import Dict, Any
import re

try:
    import dns.resolver
except Exception:
    dns = None

MANIFEST = {
    "modul_adi": "kb_email_verify",
    "versiyon": "0.1.0",
    "yazar": "KB-OSINT Team",
    "aciklama": "Email adresi var mı, MX kayıtları ve temel doğrulama kontrolleri.",
    "kategori": "email",
    "api_gereksinimleri": [],
    "bagimliliklar": ["dnspython>=2.5.0"],
    "izinler": ["dns"],
    "guvenlik_seviyesi": "orta",
    "aktif": True,
}

from core.interface import KB_Modul_Arayuzu

EMAIL_REGEX = re.compile(r"^[A-Z0-9._%+-]+@([A-Z0-9.-]+)\\.[A-Z]{2,}$", re.IGNORECASE)

class KB_EmailVerify(KB_Modul_Arayuzu):
    metadata = MANIFEST

    def calistir(self, params: Dict[str, Any]) -> Dict[str, Any]:
        self.dogrula_parametreler(params)
        email = (params.get("email") or "").strip()
        if not email or "@" not in email:
            return {"durum": "hata", "mesaj": "Geçerli bir email giriniz", "veri": {}}
        m = EMAIL_REGEX.match(email)
        if not m:
            return {"durum": "hata", "mesaj": "Email formatı geçersiz", "veri": {}}

        domain = email.split("@", 1)[1]
        out: Dict[str, Any] = {"email": email, "domain": domain, "valid_format": True, "mx_records": []}

        if dns is None:
            return {"durum": "hata", "mesaj": "dnspython yüklü değil (MX sorgusu yapılamadı)", "veri": out}

        try:
            answers = dns.resolver.resolve(domain, "MX")
            for rdata in answers:
                # rdata.exchange is a Name object, prefer string
                out["mx_records"].append(str(rdata.exchange).rstrip("."))
            status = "basarili" if out["mx_records"] else "hata"
            msg = "MX kayıtları bulundu" if out["mx_records"] else "MX kaydı bulunamadı"
            return {"durum": status, "mesaj": msg, "veri": out}
        except dns.resolver.NXDOMAIN:
            return {"durum": "hata", "mesaj": "Domain bulunamadı (NXDOMAIN)", "veri": out}
        except dns.resolver.NoAnswer:
            return {"durum": "hata", "mesaj": "MX cevabı yok (NoAnswer)", "veri": out}
        except dns.resolver.Timeout:
            return {"durum": "hata", "mesaj": "DNS sorgu zaman aşımı", "veri": out}
        except Exception as e:
            return {"durum": "hata", "mesaj": f"DNS sorgu hatası: {e}", "veri": out}