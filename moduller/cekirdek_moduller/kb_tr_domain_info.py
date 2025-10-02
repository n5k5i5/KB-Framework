"""KB-OSINT Türkiye Modülü (iskele)
Modül: kb_tr_domain_info
Türkiye domain bilgileri.
"""

MANIFEST = {
    "modul_adi": "kb_tr_domain_info",
    "versiyon": "0.1.0",
    "yazar": "KB-OSINT Team",
    "aciklama": ".tr uzantılı domainler için whois/DNS bilgilerini derler.",
    "kategori": "turkiye",
    "api_gereksinimleri": ["whois_api", "dns_api"],
    "bagimliliklar": ["dnspython>=2.1.0"],
    "izinler": ["http", "dns"],
    "guvenlik_seviyesi": "yuksek",
    "aktif": True,
}