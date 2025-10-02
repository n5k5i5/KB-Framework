from kb_osint.manager.module_manager import KB_Modul_Yoneticisi
from kb_osint.security.security_manager import KB_Guvenlik_Yoneticisi
from kb_osint.cli.shell import KB_Interaktif_Kabuk
from kb_osint.cli.color import KB_Renklendirici
from kb_osint.cli.module_commands import KB_Modul_Komutlari, KB_CLI_Entegrasyonu


class KB_OSINT_Uygulama:
    """
    Entegre uygulama iskeleti: modül yöneticisi, güvenlik yöneticisi ve CLI.
    """

    def __init__(self):
        self.guvenlik_yoneticisi = KB_Guvenlik_Yoneticisi()
        self.modul_yoneticisi = KB_Modul_Yoneticisi()
        self.kabuk = KB_Interaktif_Kabuk()

        # Modül listeleme sistemi
        self.modul_komutlari = KB_Modul_Komutlari(self)
        self.cli_entegrasyonu = KB_CLI_Entegrasyonu(self.modul_komutlari)

        self._baslangic_yuklemeleri()

    def _baslangic_yuklemeleri(self) -> None:
        """Uygulama başlangıç işlemleri"""
        self.modul_yoneticisi.modul_tara()
        self._komutlari_kaydet()

    def _komutlari_kaydet(self) -> None:
        """CLI komutlarını kaydet"""
        # Modül komutlarını kaydet
        self.cli_entegrasyonu.komutlari_kaydet(self.kabuk)

        # Yerleşik komutlar
        self.kabuk.komut_ekle("yardim", lambda _: self.kabuk.yardim(), "Yardım metnini gösterir")
        self.kabuk.komut_ekle("cikis", lambda _: None, "Kabuğu kapatır")

    def calistir(self) -> None:
        """Uygulamayı başlat"""
        self.kabuk.calistir()