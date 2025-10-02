# -*- coding: utf-8 -*-
"""
Loglama sistemi (çekirdek günlükçü).
"""
import logging
import os


class Gunlukcu:
    def __init__(self, log_dizin="kb-osint/logs"):
        os.makedirs(log_dizin, exist_ok=True)
        self.logger = logging.getLogger("KB-OSINT")
        self.logger.setLevel(logging.INFO)

        fh = logging.FileHandler(os.path.join(log_dizin, "uygulama.log"), encoding="utf-8")
        fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        fh.setFormatter(fmt)
        self.logger.addHandler(fh)

    def bilgi(self, mesaj: str):
        self.logger.info(mesaj)

    def hata(self, mesaj: str):
        self.logger.error(mesaj)