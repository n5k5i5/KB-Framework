# -*- coding: utf-8 -*-
"""Domain DNS kayıtları"""
from typing import Dict, Any, List

try:
    import dns.resolver
except Exception:
    dns = None

MANIFEST = {
    "modul_adi": "kb_domain_dns",
    "versiyon": "0.1.0",
    "yazar": "KB-OSINT Team",
    "aciklama": "Domain için A, AAAA, MX, NS, TXT, SOA kayıtlarını toplar.",
    "kategori": "domain",
    "api_gereksinimleri": [],
    "bagimliliklar": ["dnspython>=2.5.0"],
    "izinler": ["dns"],
    "guvenlik_seviyesi": "orta",
    "aktif": True,
}

from kboaint.core.interface import KB_Modul_Arayuzu

RECORD_TYPES = ["A", "AAAA", "MX", "NS", "TXT", "SOA"]

class KB_DomainDNS(KB_Modul_Arayuzu):
    metadata = MANIFEST

    def calistir(self, params: Dict[str, Any]) -> Dict[str, Any]:
        self.dogrula_parametreler(params)
        domain = (params.get("domain") or "").strip().lower()
        if not domain or "." not in domain:
            return {"durum": "hata", "mesaj": "Geçerli bir domain giriniz (örn: example.com)", "veri": {}}
        if dns is None:
            return {"durum": "hata", "mesaj": "dnspython yüklü değil", "veri": {}}

        out: Dict[str, Any] = {"domain": domain, "records": {}}
        for rtype in RECORD_TYPES:
            try:
                answers = dns.resolver.resolve(domain, rtype)
                out["records"][rtype] = self._format(rtype, answers)
            except dns.resolver.NXDOMAIN:
                out["records"][rtype] = {"status": "error", "message": "NXDOMAIN"}
            except dns.resolver.NoAnswer:
                out["records"][rtype] = {"status": "error", "message": "NoAnswer"}
            except dns.resolver.Timeout:
                out["records"][rtype] = {"status": "error", "message": "Timeout"}
            except Exception as e:
                out["records"][rtype] = {"status": "error", "message": str(e)}
        return {"durum": "basarili", "mesaj": "DNS kayıtları toplandı", "veri": out}

    def _format(self, rtype: str, answers) -> Dict[str, Any]:
        items: List[str] = []
        if rtype in {"A", "AAAA"}:
            for r in answers:
                items.append(r.address)
        elif rtype == "MX":
            for r in answers:
                items.append(f"{getattr(r,'preference','')} {str(r.exchange).rstrip('.')}")
        elif rtype == "NS":
            for r in answers:
                items.append(str(r.target).rstrip("."))
        elif rtype == "TXT":
            for r in answers:
                txts = []
                try:
                    for s in r.strings:
                        txts.append(s.decode("utf-8", errors="ignore") if isinstance(s, bytes) else str(s))
                    items.append(" ".join(txts))
                except Exception:
                    items.append(str(r))
        elif rtype == "SOA":
            r = answers[0]
            try:
                items.append(f"mname={str(r.mname).rstrip('.')} rname={str(r.rname).rstrip('.')} serial={r.serial} refresh={r.refresh} retry={r.retry} expire={r.expire} minimum={r.minimum}")
            except Exception:
                items.append(str(r))
        return {"status": "ok", "values": items}