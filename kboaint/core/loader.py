# -*- coding: utf-8 -*-
import os
import importlib.util
from typing import Dict, Any, List, Optional, Set, Type

from kboaint.core.interface import KB_Modul_Arayuzu

class Loader:
    def __init__(self, allowed_regions: Optional[List[str]] = None):
        self.modules: Dict[str, Any] = {}
        self.allowed_regions: Set[str] = set(allowed_regions or [])

    def _should_load(self, manifest: Dict[str, Any]) -> bool:
        regional = manifest.get("regional")
        if not regional:
            return True
        if not self.allowed_regions:
            return False
        return regional in self.allowed_regions

    def scan(self, dirs: List[str]) -> None:
        for d in dirs:
            if not os.path.isdir(d):
                continue
            if d.endswith(os.sep + "regional"):
                # include subfolders by country code
                for country in os.listdir(d):
                    country_dir = os.path.join(d, country)
                    if os.path.isdir(country_dir) and (not self.allowed_regions or country in self.allowed_regions):
                        self._scan_dir(country_dir)
            else:
                self._scan_dir(d)

    def _scan_dir(self, d: str) -> None:
        for root, _dirs, files in os.walk(d):
            for fn in files:
                if fn.startswith("kb_") and fn.endswith(".py"):
                    self._load_module(os.path.join(root, fn))

    def _load_module(self, path: str) -> Optional[str]:
        try:
            spec = importlib.util.spec_from_file_location("kb_modul", path)
            module = importlib.util.module_from_spec(spec)
            assert spec and spec.loader
            spec.loader.exec_module(module)

            # class-based
            for name in dir(module):
                attr = getattr(module, name)
                if isinstance(attr, type) and issubclass(attr, KB_Modul_Arayuzu) and attr is not KB_Modul_Arayuzu:
                    inst: KB_Modul_Arayuzu = attr()
                    manifest = getattr(inst, "metadata", {})
                    if not self._should_load(manifest):
                        return None
                    mod_name = manifest.get("modul_adi") or os.path.basename(path).replace(".py", "")
                    self.modules[mod_name] = inst
                    return mod_name

            # manifest-only
            man = getattr(module, "MANIFEST", None)
            if isinstance(man, dict):
                if not self._should_load(man):
                    return None
                mod_name = man.get("modul_adi") or os.path.basename(path).replace(".py", "")
                self.modules[mod_name] = man
                return mod_name
        except Exception as e:
            print(f"Modül yükleme hatası ({path}): {e}")
        return None

    def list(self) -> Dict[str, Any]:
        return self.modules.copy()