# -*- coding: utf-8 -*-
import os
from çekirdek.yükleyici import Yukleyici


def _modul_dizinleri(proje_kok: str):
    base = os.path.join(proje_kok, "modüller")
    cekirdek = os.path.join(base, "çekirdek_modüller")
    topluluk = os.path.join(base, "topluluk_modülleri")
    kullanici = os.path.join(base, "kullanıcı_modülleri")

    return [
        # Çekirdek
        os.path.join(cekirdek, "domain_osint"),
        os.path.join(cekirdek, "ip_osint"),
        os.path.join(cekirdek, "email_osint"),
        os.path.join(cekirdek, "sosyal_medya"),
        os.path.join(cekirdek, "kişi_araştırma"),
        os.path.join(cekirdek, "kurumsal_osint"),
        os.path.join(cekirdek, "gelişmiş_arama"),
        # Topluluk
        os.path.join(topluluk, "analiz_raporlama"),
        os.path.join(topluluk, "görsel_osint"),
        os.path.join(topluluk, "türkiye_özel"),
        os.path.join(topluluk, "entegrasyonlar"),
        # Kullanıcı
        os.path.join(kullanici, "kişisel_otomasyon"),
        os.path.join(kullanici, "veri_işleme"),
        os.path.join(kullanici, "entegrasyonlar"),
        os.path.join(kullanici, "özel_hedefler"),
        os.path.join(kullanici, "kişisel_raporlama"),
        os.path.join(kullanici, "iş_akışı"),
        os.path.join(kullanici, "güvenlik_gizlilik"),
    ]


def test_yukleyici_modul_yukleme():
    proje_kok = os.path.dirname(os.path.dirname(__file__))  # kb-osint/tests -> kb-osint/
    y = Yukleyici()
    y.tara(_modul_dizinleri(proje_kok))
    assert len(y.moduller) > 0, "Modüller yüklenemedi"