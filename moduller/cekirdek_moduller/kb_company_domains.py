"""KB-OSINT Çekirdek Modülü (iskele)
Modül: kb_company_domains
Şirket alan adları ve varlıklar.
"""

MANIFEST = {
    "modul_adi": "kb_company_domains",
    "versiyon": "0.1.0",
    "yazar": "KB-OSINT Team",
    "aciklama": "Şirketin sahip olduğu domainler, subdomainler ve ilişkilendirilmiş hizmetler.",
    "kategori": "kurumsal",
    "api_gereksinimleri": ["dns_api", "whois_api"],
    "bagimliliklar": ["dnspython>=2.1.0"],
    "izinler": ["http", "dns"],
    "guvenlik_seviyesi": "yuksek",
    "aktif": True,
}