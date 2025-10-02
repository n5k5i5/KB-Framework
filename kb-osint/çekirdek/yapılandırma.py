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