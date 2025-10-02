"""KB-OSINT Çekirdek Modülü (iskele)
Modül: kb_shodan_search
Shodan araması ile IP/servis OSINT.
"""

MANIFEST = {
    "modul_adi": "kb_shodan_search",
    "versiyon": "0.1.0",
    "yazar": "KB-OSINT Team",
    "aciklama": "Shodan API ile IP ve servis bilgileri toplar.",
    "kategori": "ip",
    "api_gereksinimleri": ["shodan"],
    "bagimliliklar": [],
    "izinler": ["http", "net_outbound"],
    "guvenlik_seviyesi": "yuksek",
    "aktif": True,
}