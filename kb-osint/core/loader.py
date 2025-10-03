# -*- coding: utf-8 -*-
"""
Module loader (core).
"""
from typing import Dict, Any, Iterable, Optional
import os
import importlib.util

try:
    from core.interface import KB_Modul_Arayuzu  # local base class
except Exception:
    KB_Modul_Arayuzu = None


class Loader:
    def __init__(self, allowed_regions: Optional[Iterable[str]] = None):
        # Public: name -> manifest dict (for listing)
        self.modules: Dict[str, Any] = {}
        # Internal: name -> python module object
        self._py_modules: Dict[str, Any] = {}
        # Internal: name -> class (subclass of KB_Modul_Arayuzu)
        self._classes: Dict[str, Any] = {}
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
            manifest = getattr(module, "MANIFEST", None)
            if manifest:
                manifest = dict(manifest)
            else:
                manifest = {}

            regional = manifest.get("regional")
            if regional and regional not in self.allowed_regions:
                return  # Skip due to regional restriction

            name = manifest.get("modul_adi") or os.path.basename(module_file).replace(".py", "")

            # find class implementing KB_Modul_Arayuzu
            cls = None
            if KB_Modul_Arayuzu is not None:
                for attr_name in dir(module):
                    obj = getattr(module, attr_name)
                    try:
                        if obj and isinstance(obj, type) and issubclass(obj, KB_Modul_Arayuzu) and obj is not KB_Modul_Arayuzu:
                            cls = obj
                            break
                    except Exception:
                        pass

            # Save listings and internals
            self.modules[name] = manifest or {"modul_adi": name, "aciklama": "No manifest", "aktif": True}
            self._py_modules[name] = module
            if cls:
                self._classes[name] = cls
        except Exception as e:
            print(f"Load error ({module_file}): {e}")

    def get_class(self, name: str):
        return self._classes.get(name)

    def instantiate(self, name: str, **kwargs):
        cls = self.get_class(name)
        if not cls:
            raise ValueError(f"Module '{name}' has no runnable class.")
        return cls(**kwargs)