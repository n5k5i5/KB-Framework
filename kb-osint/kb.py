"""
KB-OSINT ana uygulama (iskelet).
"""
import os
from arayüz.interaktif_kabuk import InteraktifKabuk
from arayüz.modül_lister import ModulLister
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


def main():
    proje_kok = os.path.dirname(__file__)
    yukleyici = Yukleyici()
    yukleyici.tara(_modul_dizinleri(proje_kok))

    kabuk = InteraktifKabuk()

    def _komut_modul_liste(_args=None):
        lister = ModulLister()
        lister.listele(yukleyici.moduller)

    kabuk.komut_ekle("modul_liste", _komut_modul_liste, "Yüklü modülleri listeler")
    kabuk.komut_ekle("yardim", lambda *_: kabuk.yardim(), "Yardım metnini gösterir")
    kabuk.komut_ekle("cikis", lambda *_: None, "Kabuğu kapatır")

    kabuk.calistir()


if __name__ == "__main__":
    main()