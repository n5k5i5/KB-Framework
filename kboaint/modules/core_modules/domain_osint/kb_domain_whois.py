# -*- coding: utf-8 -*-
"""Domain WHOIS/RDAP"""
from typing import Dict, Any

try:
    import requests
except Exception:
    requests = None

MANIFEST = {
    "modul_adi": "kb_domain_whois",
    "versiyon": "0.1.0",
    "yazar": "KB-OSINT Team",
    "aciklama": "RDAP üzerinden domain WHOIS bilgisi toplar.",
    "kategori": "domain",
    "api_gereksinimleri": [],
    "bagimliliklar": ["requests>=2.31.0"],
    "izinler": ["http"],
    "guvenlik_seviyesi": "orta",
    "aktif": True,
}

from kboaint.core.interface import KB_Modul_Arayuzu

class KB_DomainWhois(KB_Modul_Arayuzu):
    metadata = MANIFEST

    def calistir(self, params: Dict[str, Any]) -> Dict[str, Any]:
        self.dogrula_parametreler(params)
        domain = (params.get("domain") or "").strip().lower()
        if not domain or "." not in domain:
            return {"durum": "hata", "mesaj": "Geçerli bir domain giriniz (örn: example.com)", "veri": {}}
        if not requests:
            return {"durum": "hata", "mesaj": "requests yüklü değil", "veri": {}}
        url = f"https://rdap.org/domain/{domain}"
        try:
            r = requests.get(url, timeout=15)
            if r.status_code == 404:
                return {"durum": "hata", "mesaj": "Domain RDAP kaydı bulunamadı", "veri": {}}
            r.raise_for_status()
            data = r.json()
            return {"durum": "basarili", "mesaj": "WHOIS/RDAP verisi alındı", "veri": self._parse(data)}
        except Exception as e:
            return {"durum": "hata", "mesaj": f"RDAP isteği başarısız: {e}", "veri": {}}

    def _parse(self, data: Dict[str, Any]) -> Dict[str, Any]:
        out: Dict[str, Any] = {
            "domainName": data.get("ldhName"),
            "status": data.get("status", []),
            "nameservers": [],
            "registrar": None,
            "events": data.get("events", []),
            "contacts": [],
        }
        for ns in data.get("nameservers", []):
            ldh = ns.get("ldhName")
            if ldh:
                out["nameservers"].append(ldh)

        for ent in data.get("entities", []):
            roles = ent.get("roles", [])
            vcard = ent.get("vcardArray", [])
            name = None
            email = None
            if isinstance(vcard, list) and len(vcard) >= 2:
                for item in vcard[1]:
                    if item and isinstance(item, list):
                        if item[0] == "fn" and len(item) >= 4:
                            name = item[3]
                        if item[0] == "email" and len(item) >= 4:
                            email = item[3]
            entry = {"roles": roles, "name": name, "email": email}
            out["contacts"].append(entry)
            if "registrar" in roles or "registrant" in roles:
                out["registrar"] = out["registrar"] or name
        return out