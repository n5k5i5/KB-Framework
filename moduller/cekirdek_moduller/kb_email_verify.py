"""KB-OSINT Çekirdek Modülü (iskele)
Modül: kb_email_verify
Email adresi doğrulama ve analiz.
"""

MANIFEST = {
    "modul_adi": "kb_email_verify",
    "versiyon": "0.1.0",
    "yazar": "KB-OSINT Team",
    "aciklama": "Email adresi var mı, MX kayıtları ve temel doğrulama kontrolleri.",
    "kategori": "email",
    "api_gereksinimleri": ["dns_api"],
    "bagimliliklar": ["dnspython>=2.1.0"],
    "izinler": ["http", "dns"],
    "guvenlik_seviyesi": "yuksek",
    "aktif": True,
}