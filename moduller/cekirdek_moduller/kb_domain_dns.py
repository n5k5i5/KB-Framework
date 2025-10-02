"""KB-OSINT Çekirdek Modülü (iskele)
Modül: kb_domain_dns
Domain DNS kayıtları toplama.
"""

MANIFEST = {
    "modul_adi": "kb_domain_dns",
    "versiyon": "0.1.0",
    "yazar": "KB-OSINT Team",
    "aciklama": "Domain için A, AAAA, MX, NS, TXT vb. DNS kayıtlarını toplar.",
    "kategori": "domain",
    "api_gereksinimleri": ["dns_api"],
    "bagimliliklar": ["dnspython>=2.1.0"],
    "izinler": ["dns", "http"],
    "guvenlik_seviyesi": "yuksek",
    "aktif": True,
}