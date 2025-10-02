# -*- coding: utf-8 -*-
"""
Merkezi config yönetimi (çekirdek).
"""
import os
import yaml


class Yapilandirma:
    def __init__(self, yol="kb-osint/config/ana_config.yaml"):
        self.yol = yol
        self.veri = {}

    def yukle(self):
        if not os.path.exists(self.yol):
            self.veri = {}
            return
        with open(self.yol, "r", encoding="utf-8") as f:
            self.veri = yaml.safe_load(f) or {}

    def al(self, anahtar, varsayilan=None):
        return self.veri.get(anahtar, varsayilan)

    def kaydet(self):
        """Geçerli konfigürasyonu YAML dosyasına yazar."""
        klasor = os.path.dirname(self.yol)
        if klasor and not os.path.exists(klasor):
            os.makedirs(klasor, exist_ok=True)
        with open(self.yol, "w", encoding="utf-8") as f:
            yaml.safe_dump(self.veri or {}, f, allow_unicode=True, sort_keys=False)