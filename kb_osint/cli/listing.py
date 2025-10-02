from typing import Dict, Any, Optional, List, Tuple

from kb_osint.cli.color import KB_Renklendirici
from kb_osint.manager.module_manager import KB_Modul_Yoneticisi


def _extract_meta(modul_obj: Any) -> Dict[str, Any]:
    """
    Modül nesnesinden metadata sözlüğünü çıkarır.
    Nesne arayüzü implement ediyorsa `metadata`, değilse sözlüğü döner.
    """
    if hasattr(modul_obj, "metadata"):
        return getattr(modul_obj, "metadata", {})
    elif isinstance(modul_obj, dict):
        return modul_obj
    return {}


class KB_Modul_Lister:
    def __init__(self, modul_yoneticisi: KB_Modul_Yoneticisi):
        self.modul_yoneticisi = modul_yoneticisi

    def tum_modulleri_listele(self, detay_seviyesi: str = "normal") -> None:
        """Tüm modülleri listeler."""
        moduller = self.modul_yoneticisi.listele()
        if not moduller:
            print(KB_Renklendirici.hata("Hiç modül yüklenmemiş!"))
            return

        print(KB_Renklendirici.baslik("KB-OSINT MODÜL LİSTESİ"))
        print(KB_Renklendirici.bilgi(f"Toplam {len(moduller)} modül yüklü"))
        print("-" * 80)

        for i, modul_adi in enumerate(sorted(moduller.keys()), 1):
            modul = moduller[modul_adi]
            self._modul_bilgisi_goster(i, modul_adi, modul, detay_seviyesi)

    def modulleri_filtrele(
        self,
        kategori: Optional[str] = None,
        durum: Optional[bool] = None,
        arama_metni: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Modülleri filtreleyerek döndürür."""
        moduller = self.modul_yoneticisi.listele()
        sonuc: Dict[str, Any] = {}
        arama = (arama_metni or "").lower()

        for modul_adi, modul in moduller.items():
            meta = _extract_meta(modul)
            kat = meta.get("kategori")
            aktif = meta.get("aktif", True)
            aciklama = meta.get("aciklama", "")

            if kategori and kat != kategori:
                continue
            if durum is not None and aktif != durum:
                continue

            if arama:
                if (arama not in modul_adi.lower()) and (arama not in aciklama.lower()):
                    continue

            sonuc[modul_adi] = modul

        return sonuc

    def kategorilere_gore_listele(self) -> Dict[str, List[Tuple[str, Any]]]:
        """Modülleri kategorilerine göre gruplayarak döndürür."""
        kategoriler: Dict[str, List[Tuple[str, Any]]] = {}
        for modul_adi, modul in self.modul_yoneticisi.listele().items():
            meta = _extract_meta(modul)
            kategori = meta.get("kategori", "diger")
            kategoriler.setdefault(kategori, []).append((modul_adi, modul))
        return kategoriler

    def _modul_bilgisi_goster(self, sira: int, modul_adi: str, modul: Any, detay_seviyesi: str) -> None:
        """Tekil modül bilgisini gösterir."""
        meta = _extract_meta(modul)

        print(f"{sira:2d}. {KB_Renklendirici.bilgi(modul_adi)}")
        print(f"     {KB_Renklendirici.bilgi('Açıklama:')} {meta.get('aciklama', 'Açıklama yok')}")
        print(f"     {KB_Renklendirici.bilgi('Versiyon:')} {meta.get('versiyon', '1.0.0')}")
        print(f"     {KB_Renklendirici.bilgi('Kategori:')} {meta.get('kategori', 'genel')}")
        print(f"     {KB_Renklendirici.bilgi('Yazar:')} {meta.get('yazar', 'Bilinmiyor')}")

        if detay_seviyesi == "detayli":
            api_gerek = ", ".join(meta.get("api_gereksinimleri", [])) or "Yok"
            bagimlilik = ", ".join(meta.get("bagimliliklar", [])) or "Yok"
            guvenlik = meta.get("guvenlik_seviyesi", "orta")
            aktif_mi = meta.get("aktif", True)
            durum_metni = "🟢 Aktif" if aktif_mi else "🔴 Pasif"

            print(f"     {KB_Renklendirici.bilgi('API Gereksinimleri:')} {api_gerek}")
            print(f"     {KB_Renklendirici.bilgi('Bağımlılıklar:')} {bagimlilik}")
            print(f"     {KB_Renklendirici.bilgi('Güvenlik Seviyesi:')} {guvenlik}")
            print(f"     {KB_Renklendirici.bilgi('Durum:')} {durum_metni}")

        print()