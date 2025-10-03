# -*- coding: utf-8 -*-
"""Email doğrulama (format + MX)"""
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
    "aciklama": "E-posta formatı ve MX kayıt kontrolü",
    "kategori": "email",
    "api_gereksinimleri": [],
    "bagimliliklar": ["dnspython>=2.5.0"],
    "izinler": ["dns"],
    "guvenlik_seviyesi": "dusuk",
    "aktif": True,
}

from kboaint.core.interface import KB_Modul_Arayuzu

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

class KB_EmailVerify(KB_Modul_Arayuzu):
    metadata = MANIFEST

    def calistir(self, params: Dict[str, Any]) -> Dict[str, Any]:
        self.dogrula_parametreler(params)
        email = (params.get("email") or "").strip().lower()
        if not email or not EMAIL_RE.match(email):
            return {"durum": "hata", "mesaj": "Geçerli bir e-posta giriniz", "veri": {}}
        if dns is None:
            return {"durum": "hata", "mesaj": "dnspython yüklü değil", "veri": {}}

        domain = email.split("@", 1)[1]
        result: Dict[str, Any] = {"email": email, "domain": domain, "mx": []}
        try:
            answers = dns.resolver.resolve(domain, "MX")
            for r in answers:
                result["mx"].append(str(r.exchange).rstrip("."))
            return {"durum": "basarili", "mesaj": "E-posta doğrulandı (MX dahil)", "veri": result}
        except dns.resolver.NXDOMAIN:
            return {"durum": "hata", "mesaj": "Domain bulunamadı (NXDOMAIN)", "veri": result}
        except dns.resolver.NoAnswer:
            return {"durum": "hata", "mesaj": "MX kaydı bulunamadı", "veri": result}
        except Exception as e:
            return {"durum": "hata", "mesaj": f"MX sorgusu başarısız: {e}", "veri": result}