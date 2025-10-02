# -*- coding: utf-8 -*-
"""
Modül yükleme sistemi (çekirdek).
"""
from typing import Dict, Any, Iterable, Optional
import os
import importlib.util


class Yukleyici:
    def __init__(self, allowed_regions: Optional[Iterable[str]] = None):
        self.moduller: Dict[str, Any] = {}
        self.allowed_regions = set(allowed_regions or [])

    def tara(self, dizinler: Iterable[str]):
        """Verilen dizinleri özyinelemeli olarak tarar ve modülleri yükler."""
        for dizin in dizinler:
            if not os.path.isdir(dizin):
                continue
            for kok, _, dosyalar in os.walk(dizin):
                for dosya in dosyalar:
                    if not dosya.endswith(".py"):
                        continue
                    if not dosya.startswith("kb_"):
                        continue
                    self._yukle(os.path.join(kok, dosya))

    def _yukle(self, modul_dosyasi: str):
        try:
            spec = importlib.util.spec_from_file_location("kb_modul", modul_dosyasi)
            modul = importlib.util.module_from_spec(spec)
            assert spec and spec.loader
            spec.loader.exec_module(modul)
            if hasattr(modul, "MANIFEST"):
                manifest = dict(modul.MANIFEST)
                regional = manifest.get("regional")
                if regional and regional not in self.allowed_regions:
                    return  # Bölgesel kısıt nedeniyle yükleme
                adi = manifest.get("modul_adi") or os.path.basename(modul_dosyasi).replace(".py", "")
                self.moduller[adi] = manifest
        except Exception as e:
            print(f"Yükleme hatası ({modul_dosyasi}): {e}")