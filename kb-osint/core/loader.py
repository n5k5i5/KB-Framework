# -*- coding: utf-8 -*-
"""
Module loader (core).
"""
from typing import Dict, Any, Iterable, Optional
import os
import importlib.util


class Loader:
    def __init__(self, allowed_regions: Optional[Iterable[str]] = None):
        self.modules: Dict[str, Any] = {}
        self.allowed_regions = set(allowed_regions or [])

    def scan(self, directories: Iterable[str]):
        """Recursively scan given directories and load modules."""
        for d in directories:
            if not os.path.isdir(d):
                continue
            for root, _, files in os.walk(d):
                for fname in files:
                    if not fname.endswith(".py"):
                        continue
                    if not fname.startswith("kb_"):
                        continue
                    self._load(os.path.join(root, fname))

    def _load(self, module_file: str):
        try:
            spec = importlib.util.spec_from_file_location("kb_module", module_file)
            module = importlib.util.module_from_spec(spec)
            assert spec and spec.loader
            spec.loader.exec_module(module)
            if hasattr(module, "MANIFEST"):
                manifest = dict(module.MANIFEST)
                regional = manifest.get("regional")
                if regional and regional not in self.allowed_regions:
                    return  # Skip due to regional restriction
                name = manifest.get("modul_adi") or os.path.basename(module_file).replace(".py", "")
                self.modules[name] = manifest
        except Exception as e:
            print(f"Load error ({module_file}): {e}")