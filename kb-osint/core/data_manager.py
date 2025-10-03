# -*- coding: utf-8 -*-
"""
Veritabanı işlemleri (çekirdek veri yöneticisi).
"""
from datetime import datetime


class VeriYoneticisi:
    def __init__(self):
        self._hafiza = {
            "hedefler": [],
            "sonuclar": [],
        }

    def hedef_ekle(self, hedef: str, tip: str = "domain", etiketler=None) -> int:
        kayit = {
            "id": len(self._hafiza["hedefler"]) + 1,
            "hedef": hedef,
            "tip": tip,
            "eklenme_tarihi": datetime.now().isoformat(),
            "etiketler": etiketler or [],
        }
        self._hafiza["hedefler"].append(kayit)
        return kayit["id"]

    def sonuc_kaydet(self, hedef_id: int, modul_adi: str, sonuc: dict, basarili: bool = True, hata: str = None):
        self._hafiza["sonuclar"].append({
            "hedef_id": hedef_id,
            "modul_adi": modul_adi,
            "tarih": datetime.now().isoformat(),
            "sonuc": sonuc,
            "basarili": basarili,
            "hata": hata,
        })