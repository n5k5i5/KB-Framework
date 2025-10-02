"""KB-OSINT Protokol Modülü (iskele)
Modül: kb_iot_device_search
IoT cihaz arama ve keşfi.
"""

MANIFEST = {
    "modul_adi": "kb_iot_device_search",
    "versiyon": "0.1.0",
    "yazar": "KB-OSINT Team",
    "aciklama": "Açık IoT cihazları ve servisleri için arama ve keşif yapar.",
    "kategori": "protokoller",
    "api_gereksinimleri": ["shodan", "censys"],
    "bagimliliklar": [],
    "izinler": ["http", "net_outbound"],
    "guvenlik_seviyesi": "yuksek",
    "aktif": True,
}