# -*- coding: utf-8 -*-
"""
Modül komutları ve CLI entegrasyonu.
"""
from arayüz.modül_lister import ModulLister
from arayüz.renklendirici import Renklendirici


class ModulKomutlari:
    def __init__(self, yukleyici):
        self.yukleyici = yukleyici
        self.lister = ModulLister()

    def modul_liste(self, parametreler=None):
        if not parametreler:
            self.lister.listele(self.yukleyici.moduller)
            return
        alt = parametreler[0]
        if alt == "detayli":
            self.lister.listele(self.yukleyici.moduller, detay_seviyesi="detayli")
        elif alt == "kategori":
            if len(parametreler) > 1:
                self._kategori_liste(parametreler[1])
            else:
                self._kategorileri_listele()
        elif alt == "ara":
            if len(parametreler) > 1:
                self._ara(parametreler[1])
            else:
                print(Renklendirici.hata("Arama metni gerekli: modul_liste ara <metin>"))
        elif alt == "aktif":
            self._aktif_liste()
        elif alt == "pasif":
            self._pasif_liste()
        else:
            print(Renklendirici.hata("Geçersiz alt komut. Kullanım: modul_liste [detayli|kategori|ara|aktif|pasif]"))

    def _kategorileri_listele(self):
        kategoriler = self.lister.kategorilere_gore(self.yukleyici.moduller)
        print(Renklendirici.baslik("MODÜL KATEGORİLERİ"))
        print("=" * 30)
        for kategori, modul_listesi in sorted(kategoriler.items()):
            print(f"📁 {kategori}: {len(modul_listesi)} modül")

    def _kategori_liste(self, kategori: str):
        kategoriler = self.lister.kategorilere_gore(self.yukleyici.moduller)
        if kategori not in kategoriler:
            mevcut = ", ".join(sorted(kategoriler.keys())) or "(yok)"
            print(Renklendirici.hata(f"'{kategori}' kategorisi bulunamadı!"))
            print(Renklendirici.bilgi(f"Mevcut kategoriler: {mevcut}"))
            return
        print(Renklendirici.baslik(f"{kategori.upper()} KATEGORİSİ MODÜLLERİ"))
        print("=" * 50)
        for i, (ad, modul) in enumerate(sorted(kategoriler[kategori]), 1):
            self.lister._tek_modul_bilgisi(i, ad, modul, "normal")

    def _ara(self, metin: str):
        sonuc = self.lister.filtrele(self.yukleyici.moduller, arama_metni=metin)
        if not sonuc:
            print(Renklendirici.hata(f"'{metin}' ile eşleşen modül bulunamadı!"))
            return
        print(Renklendirici.baslik(f"'{metin}' ARAMA SONUÇLARI ({len(sonuc)} modül)"))
        print("=" * 60)
        for i, ad in enumerate(sorted(sonuc.keys()), 1):
            self.lister._tek_modul_bilgisi(i, ad, sonuc[ad], "normal")

    def _aktif_liste(self):
        aktif = self.lister.filtrele(self.yukleyici.moduller, durum=True)
        print(Renklendirici.baslik(f"AKTİF MODÜLLER ({len(aktif)} modül)"))
        print("=" * 40)
        for i, ad in enumerate(sorted(aktif.keys()), 1):
            self.lister._tek_modul_bilgisi(i, ad, aktif[ad], "normal")

    def _pasif_liste(self):
        pasif = self.lister.filtrele(self.yukleyici.moduller, durum=False)
        if not pasif:
            print(Renklendirici.bilgi("Pasif modül bulunamadı!"))
            return
        print(Renklendirici.baslik(f"PASİF MODÜLLER ({len(pasif)} modül)"))
        print("=" * 40)
        for i, ad in enumerate(sorted(pasif.keys()), 1):
            self.lister._tek_modul_bilgisi(i, ad, pasif[ad], "normal")