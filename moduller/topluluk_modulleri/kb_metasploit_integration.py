"""KB-OSINT Topluluk Modülü (iskele)
Modül: kb_metasploit_integration
Metasploit entegrasyonu (topluluk).
"""

MANIFEST = {
    "modul_adi": "kb_metasploit_integration",
    "versiyon": "0.1.0",
    "yazar": "Topluluk",
    "aciklama": "Metasploit ile bilgi toplama ve çıktı zenginleştirme.",
    "kategori": "topluluk_entegrasyon",
    "api_gereksinimleri": ["metasploit_api"],
    "bagimliliklar": [],
    "izinler": ["subprocess", "net_outbound"],
    "guvenlik_seviyesi": "orta",
    "aktif": True,
}