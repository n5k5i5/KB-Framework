# -*- coding: utf-8 -*-
"""
Güvenlik yöneticisi (çekirdek).
"""
import hashlib


class GuvenlikYoneticisi:
    def modul_imzala(self, modul_yolu: str) -> str:
        with open(modul_yolu, "rb") as f:
            icerik = f.read()
        imza = hashlib.sha256(icerik).hexdigest()
        return f"KB_MODUL_{imza}"

    def modul_dogrula(self, resmi_imza: str, sunulan_imza: str) -> bool:
        return bool(resmi_imza) and resmi_imza == sunulan_imza