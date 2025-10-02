"""KB-OSINT Çekirdek Modülü (iskele)
Modül: kb_subdomain_scan
Subdomain keşfi ve haritalama.
"""

MANIFEST = {
    "modul_adi": "kb_subdomain_scan",
    "versiyon": "0.1.0",
    "yazar": "KB-OSINT Team",
    "aciklama": "Hedef domain için alt alan adlarını keşfeder ve doğrular.",
    "kategori": "domain",
    "api_gereksinimleri": ["dns_api", "search_api"],
    "bagimliliklar": ["dnspython>=2.1.0"],
    "izinler": ["dns", "http"],
    "guvenlik_seviyesi": "yuksek",
    "aktif": True,
}