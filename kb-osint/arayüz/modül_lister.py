# -*- coding: utf-8 -*-
"""
Modül listeleyici ve filtreleyici.
"""
from typing import Dict, Any, Optional, List, Tuple
from arayüz.renklendirici import Renklendirici


def _meta(modul: Any) -> Dict[str, Any]:
    return modul if isinstance(modul, dict) else {}


class ModulLister:
    def listele(self, moduller: Dict[str, Any], detay_seviyesi: str = "normal") -> None:
        if not moduller:
            print(Renklendirici.hata("Hiç modül yüklenmemiş!"))
            return

        print(Renklendirici.baslik("KB-OSINT MODÜL LİSTESİ"))
        print(Renklendirici.bilgi(f"Toplam {len(moduller)} modül yüklü"))
        print("-" * 80)

        for i, ad in enumerate(sorted(moduller.keys()), 1):
            self._tek_modul_bilgisi(i, ad, moduller[ad], detay_seviyesi)

    def filtrele(
        self,
        moduller: Dict[str, Any],
        kategori: Optional[str] = None,
        durum: Optional[bool] = None,
        arama_metni: Optional[str] = None,
    ) -> Dict[str, Any]:
        sonuc: Dict[str, Any] = {}
        arama = (arama_metni or "").lower()

        for ad, modul in moduller.items():
            meta = _meta(modul)
            kat = meta.get("kategori")
            aktif = meta.get("aktif", True)
            aciklama = meta.get("aciklama", "")

            if kategori and kat != kategori:
                continue
            if durum is not None and aktif != durum:
                continue

            if arama:
                if (arama not in ad.lower()) and (arama not in aciklama.lower()):
                    continue

            sonuc[ad] = modul

        return sonuc

    def kategorilere_gore(self, moduller: Dict[str, Any]) -> Dict[str, List[Tuple[str, Any]]]:
        kategoriler: Dict[str, List[Tuple[str, Any]]] = {}
        for ad, modul in moduller.items():
            meta = _meta(modul)
            kategori = meta.get("kategori", "diger")
            kategoriler.setdefault(kategori, []).append((ad, modul))
        return kategoriler

    def _tek_modul_bilgisi(self, sira: int, ad: str, modul: Any, detay_seviyesi: str) -> None:
        meta = _meta(modul)
        print(f"{sira:2d}. {Renklendirici.vurgu(ad)}")
        print(f"     {Renklendirici.bilgi('Açıklama:')} {meta.get('aciklama', 'Açıklama yok')}")
        print(f"     {Renklendirici.bilgi('Versiyon:')} {meta.get('versiyon', '1.0.0')}")
        print(f"     {Renklendirici.bilgi('Kategori:')} {meta.get('kategori', 'genel')}")
        print(f"     {Renklendirici.bilgi('Yazar:')} {meta.get('yazar', 'Bilinmiyor')}")

        if detay_seviyesi == "detayli":
            api_gerek = ", ".join(meta.get("api_gereksinimleri", [])) or "Yok"
            bagimlilik = ", ".join(meta.get("bagimliliklar", [])) or "Yok"
            guvenlik = meta.get("guvenlik_seviyesi", "orta")
            aktif_mi = meta.get("aktif", True)
            durum_metni = "🟢 Aktif" if aktif_mi else "🔴 Pasif"

            print(f"     {Renklendirici.bilgi('API Gereksinimleri:')} {api_gerek}")
            print(f"     {Renklendirici.bilgi('Bağımlılıklar:')} {bagimlilik}")
            print(f"     {Renklendirici.bilgi('Güvenlik Seviyesi:')} {guvenlik}")
            print(f"     {Renklendirici.bilgi('Durum:')} {durum_metni}")

        print()