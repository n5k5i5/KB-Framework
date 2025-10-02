from kb_osint.cli.listing import KB_Modul_Lister
from kb_osint.cli.color import KB_Renklendirici


class KB_Modul_Komutlari:
    def __init__(self, uygulama):
        self.uygulama = uygulama
        self.lister = KB_Modul_Lister(uygulama.modul_yoneticisi)

    def modul_liste_komutu(self, parametreler):
        """Ana modül listeleme komutu."""
        if not parametreler:
            self.lister.tum_modulleri_listele()
            return

        alt = parametreler[0]

        if alt == "detayli":
            self.lister.tum_modulleri_listele(detay_seviyesi="detayli")

        elif alt == "kategori":
            if len(parametreler) > 1:
                kategori = parametreler[1]
                self._kategori_modulleri_listele(kategori)
            else:
                self._tum_kategorileri_listele()

        elif alt == "ara":
            if len(parametreler) > 1:
                arama = parametreler[1]
                self._modul_ara(arama)
            else:
                print(KB_Renklendirici.hata("Arama metni gerekli: modul_liste ara <metin>"))

        elif alt == "aktif":
            self._aktif_modulleri_listele()

        elif alt == "pasif":
            self._pasif_modulleri_listele()

        else:
            print(KB_Renklendirici.hata("Geçersiz alt komut. Kullanım: modul_liste [detayli|kategori|ara|aktif|pasif]"))

    def _kategori_modulleri_listele(self, kategori: str):
        """Belirli kategorideki modülleri listeler."""
        kategoriler = self.lister.kategorilere_gore_listele()

        if kategori not in kategoriler:
            print(KB_Renklendirici.hata(f"'{kategori}' kategorisi bulunamadı!"))
            mevcut = ", ".join(sorted(kategoriler.keys())) or "(yok)"
            print(KB_Renklendirici.bilgi(f"Mevcut kategoriler: {mevcut}"))
            return

        print(KB_Renklendirici.baslik(f"{kategori.upper()} KATEGORİSİ MODÜLLERİ"))
        print("=" * 50)

        for i, (modul_adi, modul) in enumerate(sorted(kategoriler[kategori]), 1):
            self.lister._modul_bilgisi_goster(i, modul_adi, modul, "normal")

    def _tum_kategorileri_listele(self):
        """Tüm kategorileri ve modül sayılarını listeler."""
        kategoriler = self.lister.kategorilere_gore_listele()

        print(KB_Renklendirici.baslik("MODÜL KATEGORİLERİ"))
        print("=" * 30)

        for kategori, modul_listesi in sorted(kategoriler.items()):
            print(f"📁 {kategori}: {len(modul_listesi)} modül")

    def _modul_ara(self, arama_metni: str):
        """Modüllerde arama yapar."""
        filtrelenmis = self.lister.modulleri_filtrele(arama_metni=arama_metni)

        if not filtrelenmis:
            print(KB_Renklendirici.hata(f"'{arama_metni}' ile eşleşen modül bulunamadı!"))
            return

        print(KB_Renklendirici.baslik(f"'{arama_metni}' ARAMA SONUÇLARI ({len(filtrelenmis)} modül)"))
        print("=" * 60)

        for i, modul_adi in enumerate(sorted(filtrelenmis.keys()), 1):
            modul = filtrelenmis[modul_adi]
            self.lister._modul_bilgisi_goster(i, modul_adi, modul, "normal")

    def _aktif_modulleri_listele(self):
        """Sadece aktif modülleri listeler."""
        aktif = self.lister.modulleri_filtrele(durum=True)
        print(KB_Renklendirici.baslik(f"AKTİF MODÜLLER ({len(aktif)} modül)"))
        print("=" * 40)
        for i, modul_adi in enumerate(sorted(aktif.keys()), 1):
            modul = aktif[modul_adi]
            self.lister._modul_bilgisi_goster(i, modul_adi, modul, "normal")

    def _pasif_modulleri_listele(self):
        """Sadece pasif modülleri listeler."""
        pasif = self.lister.modulleri_filtrele(durum=False)
        if not pasif:
            print(KB_Renklendirici.bilgi("Pasif modül bulunamadı!"))
            return
        print(KB_Renklendirici.baslik(f"PASİF MODÜLLER ({len(pasif)} modül)"))
        print("=" * 40)
        for i, modul_adi in enumerate(sorted(pasif.keys()), 1):
            modul = pasif[modul_adi]
            self.lister._modul_bilgisi_goster(i, modul_adi, modul, "normal")


class KB_CLI_Entegrasyonu:
    def __init__(self, modul_komutlari: KB_Modul_Komutlari):
        self.komutlar = modul_komutlari

    def komutlari_kaydet(self, kabuk) -> None:
        """CLI komutlarını kaydeder."""
        kabuk.komut_ekle(
            "modul_liste",
            self.komutlar.modul_liste_komutu,
            "Modülleri listeler - modul_liste [detayli|kategori|ara|aktif|pasif]",
        )
        kabuk.komut_ekle(
            "modul_kategoriler",
            self._kategorileri_goster,
            "Tüm modül kategorilerini listeler",
        )
        kabuk.komut_ekle(
            "modul_ara",
            self._modul_ara_komutu,
            "Modüllerde arama yapar - modul_ara <metin>",
        )

    def _kategorileri_goster(self, _parametreler):
        """Kategori listeleme komutu."""
        self.komutlar._tum_kategorileri_listele()

    def _modul_ara_komutu(self, parametreler):
        """Modül arama komutu."""
        if not parametreler:
            print(KB_Renklendirici.hata("Arama metni gerekli: modul_ara <metin>"))
            return
        self.komutlar._modul_ara(parametreler[0])