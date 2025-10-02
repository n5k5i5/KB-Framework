"""
KB-OSINT ana uygulama (iskelet).
"""
import os
from arayüz.interaktif_kabuk import InteraktifKabuk
from çekirdek.yükleyici import Yukleyici
from çekirdek.yapılandırma import Yapilandirma
from arayüz.modul_komutlari import ModulKomutlari


def _modul_dizinleri(proje_kok: str, enabled_countries=None):
    enabled_countries = set(enabled_countries or [])
    base = os.path.join(proje_kok, "modüller")
    cekirdek = os.path.join(base, "çekirdek_modüller")
    topluluk = os.path.join(base, "topluluk_modülleri")
    kullanici = os.path.join(base, "kullanıcı_modülleri")

    dizinler = [
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

    # Bölgesel (ülke) modüllerini opsiyonel olarak ekle
    if "tr" in enabled_countries:
        dizinler.append(os.path.join(base, "regional", "tr"))

    return dizinler


def main():
    proje_kok = os.path.dirname(__file__)

    # Config yükle ve bölgesel ayarları al
    cfg = Yapilandirma()
    cfg.yukle()
    regional = cfg.al("regional", {}) or {}
    enabled_countries = regional.get("enabled_countries", [])

    yukleyici = Yukleyici(allowed_regions=enabled_countries)
    yukleyici.tara(_modul_dizinleri(proje_kok, enabled_countries))

    kabuk = InteraktifKabuk()
    mk = ModulKomutlari(yukleyici)

    # Komutlar (TR ve EN takma adlar)
    kabuk.komut_ekle("modul_liste", mk.modul_liste, "Modülleri listeler - modul_liste [detayli|kategori|ara|aktif|pasif]")
    kabuk.komut_ekle("module_list", mk.modul_liste, "List modules - module_list [detailed|category|search|active|inactive]")
    kabuk.komut_ekle("modul_kategoriler", lambda *_: mk._kategorileri_listele(), "Tüm modül kategorilerini listeler")
    kabuk.komut_ekle("module_categories", lambda *_: mk._kategorileri_listele(), "List all module categories")
    kabuk.komut_ekle("modul_ara", lambda args: mk._ara(args[0] if args else ""), "Modüllerde arama yapar - modul_ara <metin>")
    kabuk.komut_ekle("module_search", lambda args: mk._ara(args[0] if args else ""), "Search modules - module_search <text>")

    # Yerleşik komutlar (TR ve EN)
    kabuk.komut_ekle("yardim", lambda *_: kabuk.yardim(), "Yardım metnini gösterir")
    kabuk.komut_ekle("help", lambda *_: kabuk.yardim(), "Show help")
    kabuk.komut_ekle("cikis", lambda *_: None, "Kabuğu kapatır")
    kabuk.komut_ekle("exit", lambda *_: None, "Exit shell")

    kabuk.calistir()


if __name__ == "__main__":
    main()