from kb_osint.manager.module_manager import KB_Modul_Yoneticisi
from kb_osint.security.security_manager import KB_Guvenlik_Yoneticisi
from kb_osint.cli.shell import KB_Interaktif_Kabuk
from kb_osint.cli.color import KB_Renklendirici


class KB_OSINT_Uygulama:
    """
    Entegre uygulama iskeleti: modül yöneticisi, güvenlik yöneticisi ve CLI.
    """

    def __init__(self):
        self.guvenlik_yoneticisi = KB_Guvenlik_Yoneticisi()
        self.modul_yoneticisi = KB_Modul_Yoneticisi()
        self.kabuk = KB_Interaktif_Kabuk()

        self._baslangic_yuklemeleri()

    def _baslangic_yuklemeleri(self) -> None:
        """Uygulama başlangıç işlemleri"""
        self.modul_yoneticisi.modul_tara()
        self._komutlari_kaydet()

    def _komutlari_kaydet(self) -> None:
        """CLI komutlarını kaydet"""
        self.kabuk.komut_ekle("modul_liste", self._komut_modul_liste, "Yüklü modülleri listeler")
        self.kabuk.komut_ekle("yardim", lambda _: self.kabuk.yardim(), "Yardım metnini gösterir")
        self.kabuk.komut_ekle("cikis", lambda _: None, "Kabuğu kapatır")

    # Komut işlevleri
    def _komut_modul_liste(self, args):
        moduller = self.modul_yoneticisi.listele()
        if not moduller:
            print(KB_Renklendirici.bilgi("Herhangi bir modül yüklenmemiş."))
            return
        print(KB_Renklendirici.baslik("Yüklü Modüller:"))
        for adi, nesne in sorted(moduller.items()):
            if hasattr(nesne, "metadata"):
                aciklama = nesne.metadata.get("aciklama", "")
            elif isinstance(nesne, dict):
                aciklama = nesne.get("aciklama", "")
            else:
                aciklama = ""
            print(f"  - {adi:16} {aciklama}")

    def calistir(self) -> None:
        """Uygulamayı başlat"""
        self.kabuk.calistir()