"""KB-OSINT Çekirdek Modülü (iskele)
Modül: kb_domain_whois
Domain WHOIS bilgileri toplama.
"""

MANIFEST = {
    "modul_adi": "kb_domain_whois",
    "versiyon": "0.1.0",
    "yazar": "KB-OSINT Team",
    "aciklama": "Domain WHOIS bilgilerini toplar.",
    "kategori": "domain",
    "api_gereksinimleri": ["whois_api"],
    "bagimliliklar": ["python-whois>=0.8.0"],
    "izinler": ["http", "dns"],
    "guvenlik_seviyesi": "yuksek",
    "aktif": True,
}