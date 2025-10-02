"""KB-OSINT Protokol Modülü (iskele)
Modül: kb_satellite_imagery
Uydu görüntüleri ve konum doğrulama.
"""

MANIFEST = {
    "modul_adi": "kb_satellite_imagery",
    "versiyon": "0.1.0",
    "yazar": "KB-OSINT Team",
    "aciklama": "Uydu görüntüleri ile konum doğrulama ve değişiklik analizi.",
    "kategori": "protokoller",
    "api_gereksinimleri": ["satellite_api"],
    "bagimliliklar": [],
    "izinler": ["http", "net_outbound"],
    "guvenlik_seviyesi": "yuksek",
    "aktif": True,
}