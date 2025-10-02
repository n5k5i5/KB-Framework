"""KB-OSINT Raporlama Modülü (iskele)
Modül: kb_alert_system
Bildirim ve uyarı sistemi.
"""

MANIFEST = {
    "modul_adi": "kb_alert_system",
    "versiyon": "0.1.0",
    "yazar": "KB-OSINT Team",
    "aciklama": "Kritik bulgular için Slack/Discord/Email uyarılarını tetikler.",
    "kategori": "raporlama",
    "api_gereksinimleri": ["messaging_api"],
    "bagimliliklar": [],
    "izinler": ["http", "net_outbound"],
    "guvenlik_seviyesi": "yuksek",
    "aktif": True,
}