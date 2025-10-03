# -*- coding: utf-8 -*-
"""
API entegrasyon yöneticisi (çekirdek).
"""
import requests


class APIYoneticisi:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "KB-OSINT/1.0.0",
            "Accept": "application/json",
        })

    def get(self, url: str, **kwargs):
        try:
            r = self.session.get(url, timeout=30, **kwargs)
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            return {"hata": str(e)}