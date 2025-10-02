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
        alt = (parametreler[0] or "").lower()

        # Alt komut eş anlamlıları (TR/EN)
        if alt in {"detayli", "detailed"}:
            self.lister.listele(self.yukleyici.moduller, detay_seviyesi="detayli")
        elif alt in {"kategori", "category"}:
            if len(parametreler) > 1:
                self._kategori_liste(parametreler[1])
            else:
                self._kategorileri_listele()
        elif alt in {"ara", "search"}:
            if len(parametreler) > 1:
                self._ara(parametreler[1])
            else:
                print(Renklendirici.hata("Arama metni gerekli: modul_liste ara|search <metin>"))
        elif alt in {"aktif", "active"}:
            self._aktif_liste()
        elif alt in {"pasif", "inactive"}:
            self._pasif_liste()
        else:
            print(Renklendirici.hata("Geçersiz alt komut. Kullanım: modul_liste [detayli|detailed|kategori|category|ara|search|aktif|active|pasif|inactive]"))

    def _kategorileri_listele(self):
        kategoriler = self.lister.kategorilere_gore(self.yukleyici.moduller)
        print(Renklendirici.baslik("MODÜL KATEGORİLERİ / MODULE CATEGORIES"))
        print("=" * 30)
        for kategori, modul_listesi in sorted(kategoriler.items()):
            print(f"📁 {kategori}: {len(modul_listesi)} modül")

    def _kategori_liste(self, kategori: str):
        kategoriler = self.lister.kategorilere_gore(self.yukleyici.moduller)
        if kategori not in kategoriler:
            mevcut = ", ".join(sorted(kategoriler.keys())) or "(none)"
            print(Renklendirici.hata(f"'{kategori}' kategorisi bulunamadı / category not found!"))
            print(Renklendirici.bilgi(f"Mevcut kategoriler / available: {mevcut}"))
            return
        print(Renklendirici.baslik(f"{kategori.upper()} KATEGORİSİ MODÜLLERİ"))
        print("=" * 50)
        for i, (ad, modul) in enumerate(sorted(kategoriler[kategori]), 1):
            self.lister._tek_modul_bilgisi(i, ad, modul, "normal")

    def _ara(self, metin: str):
        sonuc = self.lister.filtrele(self.yukleyici.moduller, arama_metni=metin)
        if not sonuc:
            print(Renklendirici.hata(f"'{metin}' ile eşleşen modül bulunamadı! / no matches"))
            return
        print(Renklendirici.baslik(f"'{metin}' ARAMA SONUÇLARI / SEARCH RESULTS ({len(sonuc)} modül)"))
        print("=" * 60)
        for i, ad in enumerate(sorted(sonuc.keys()), 1):
            self.lister._tek_modul_bilgisi(i, ad, sonuc[ad], "normal")

    def _aktif_liste(self):
        aktif = self.lister.filtrele(self.yukleyici.moduller, durum=True)
        print(Renklendirici.baslik(f"AKTİF / ACTIVE MODÜLLER ({len(aktif)} modül)"))
        print("=" * 40)
        for i, ad in enumerate(sorted(aktif.keys()), 1):
            self.lister._tek_modul_bilgisi(i, ad, aktif[ad], "normal")

    def _pasif_liste(self):
        pasif = self.lister.filtrele(self.yukleyici.moduller, durum=False)
        if not pasif:
            print(Renklendirici.bilgi("Pasif modül bulunamadı / no inactive modules"))
            return
        print(Renklendirici.baslik(f"PASİF / INACTIVE MODÜLLER ({len(pasif)} modül)"))
        print("=" * 40)
        for i, ad in enumerate(sorted(pasif.keys()), 1):
            self.lister._tek_modul_bilgisi(i, ad, pasif[ad], "normal")