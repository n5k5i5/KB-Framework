"""KB-OSINT Çekirdek Modülü (iskele)
Modül: kb_censys_search
Censys araması ile varlık keşfi.
"""

MANIFEST = {
    "modul_adi": "kb_censys_search",
    "versiyon": "0.1.0",
    "yazar": "KB-OSINT Team",
    "aciklama": "Censys API ile IP/host sertifika ve varlık araması yapar.",
    "kategori": "ip",
    "api_gereksinimleri": ["censys"],
    "bagimliliklar": [],
    "izinler": ["http", "net_outbound"],
    "guvenlik_seviyesi": "yuksek",
    "aktif": True,
}