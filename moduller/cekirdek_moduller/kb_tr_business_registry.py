"""KB-OSINT API Modülü (iskele)
Modül: kb_tr_business_registry
Türkiye ticari sicil entegrasyonu.
"""

MANIFEST = {
    "modul_adi": "kb_tr_business_registry",
    "versiyon": "0.1.0",
    "yazar": "KB-OSINT Team",
    "aciklama": "Türkiye ticaret sicil kayıtları ile şirket doğrulama ve arama.",
    "kategori": "api",
    "api_gereksinimleri": ["tr_business_api"],
    "bagimliliklar": [],
    "izinler": ["http", "net_outbound"],
    "guvenlik_seviyesi": "yuksek",
    "aktif": True,
}