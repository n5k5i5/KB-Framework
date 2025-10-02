"""
KB-OSINT CLI giriş noktası.
"""
import os
from arayüz.interaktif_kabuk import InteraktifKabuk
from çekirdek.yükleyici import Yukleyici
from arayüz.modul_komutlari import ModulKomutlari


def _modul_dizinleri(proje_kok: str):
    base = os.path.join(proje_kok, "modüller")
    cekirdek = os.path.join(base, "çekirdek_modüller")
    topluluk = os.path.join(base, "topluluk_modülleri")
    kullanici = os.path.join(base, "kullanıcı_modülleri")

    return [
        os.path.join(cekirdek, "domain_osint"),
        os.path.join(cekirdek, "ip_osint"),
        os.path.join(cekirdek, "email_osint"),
        os.path.join(cekirdek, "sosyal_medya"),
        os.path.join(cekirdek, "kişi_araştırma"),
        os.path.join(cekirdek, "kurumsal_osint"),
        os.path.join(cekirdek, "gelişmiş_arama"),
        os.path.join(topluluk, "analiz_raporlama"),
        os.path.join(topluluk, "görsel_osint"),
        os.path.join(topluluk, "türkiye_özel"),
        os.path.join(topluluk, "entegrasyonlar"),
        os.path.join(kullanici, "kişisel_otomasyon"),
        os.path.join(kullanici, "veri_işleme"),
        os.path.join(kullanici, "entegrasyonlar"),
        os.path.join(kullanici, "özel_hedefler"),
        os.path.join(kullanici, "kişisel_raporlama"),
        os.path.join(kullanici, "iş_akışı"),
        os.path.join(kullanici, "güvenlik_gizlilik"),
    ]


def run():
    proje_kok = os.path.dirname(__file__)
    y = Yukleyici()
    y.tara(_modul_dizinleri(proje_kok))

    shell = InteraktifKabuk()
    mk = ModulKomutlari(y)
    shell.komut_ekle("modul_liste", mk.modul_liste, "Modülleri listeler - modul_liste [detayli|kategori|ara|aktif|pasif]")
    shell.komut_ekle("modul_kategoriler", lambda *_: mk._kategorileri_listele(), "Tüm modül kategorilerini listeler")
    shell.komut_ekle("modul_ara", lambda args: mk._ara(args[0] if args else ""), "Modüllerde arama yapar - modul_ara <metin>")
    shell.komut_ekle("yardim", lambda *_: shell.yardim(), "Yardım metnini gösterir")
    shell.komut_ekle("cikis", lambda *_: None, "Kabuğu kapatır")
    shell.calistir()


if __name__ == "__main__":
    run()