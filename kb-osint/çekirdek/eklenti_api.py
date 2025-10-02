# -*- coding: utf-8 -*-
"""
Geliştirici eklenti API'si (çekirdek arayüz).
"""


class KB_Modul_Arayuzu:
    def __init__(self):
        self.metadata = {
            "modul_adi": "",
            "versiyon": "1.0.0",
            "yazar": "",
            "aciklama": "",
            "kategori": "",
            "api_gereksinimleri": [],
            "bagimliliklar": [],
            "izinler": [],
            "guvenlik_seviyesi": "orta",
            "aktif": True,
        }

    def initialize(self):
        pass

    def execute(self, hedef, parametreler=None):
        if parametreler is None:
            parametreler = {}
        raise NotImplementedError

    def validate(self):
        return True

    def cleanup(self):
        pass