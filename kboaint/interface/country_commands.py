# -*- coding: utf-8 -*-
from typing import List
import os

from kboaint.core.loader import Loader
from kboaint.core.config_manager import ConfigManager

class CountryCommands:
    def __init__(self, loader: Loader, cfg: ConfigManager, base_dir: str):
        self.loader = loader
        self.cfg = cfg
        self.base_dir = base_dir

    def country_list(self, _args: List[str]) -> None:
        reg = self.cfg.get("regional", {}) or {}
        mode = reg.get("mode", "international")
        if mode == "national":
            print(f"Mode: national, country: {reg.get('country_code')}")
        else:
            enabled = reg.get("enabled_countries", []) or []
            print(f"Mode: international, enabled: {enabled}")

    def country_enable(self, args: List[str]) -> None:
        if not args:
            print("Usage: country_enable <code>")
            return
        reg = self.cfg.get("regional", {}) or {}
        if reg.get("mode", "international") == "national":
            print("National mode is active. Use country_set instead.")
            return
        enabled = reg.get("enabled_countries", []) or []
        code = args[0]
        if code not in enabled:
            enabled.append(code)
        reg["enabled_countries"] = enabled
        self.cfg.set("regional", reg)
        self.cfg.save()
        print(f"Enabled countries: {enabled}")

    def country_disable(self, args: List[str]) -> None:
        if not args:
            print("Usage: country_disable <code>")
            return
        reg = self.cfg.get("regional", {}) or {}
        enabled = reg.get("enabled_countries", []) or []
        code = args[0]
        enabled = [c for c in enabled if c != code]
        reg["enabled_countries"] = enabled
        self.cfg.set("regional", reg)
        self.cfg.save()
        print(f"Enabled countries: {enabled}")

    def country_set(self, args: List[str]) -> None:
        if not args:
            print("Usage: country_set <code>")
            return
        code = args[0]
        reg = self.cfg.get("regional", {}) or {}
        reg["mode"] = "national"
        reg["country_code"] = code
        self.cfg.set("regional", reg)
        self.cfg.save()
        print(f"National mode set: country={code}")

    def reload_modules(self, _args: List[str]) -> None:
        reg = self.cfg.get("regional", {}) or {}
        mode = reg.get("mode", "international")
        allowed = []
        if mode == "national" and reg.get("country_code"):
            allowed = [reg["country_code"]]
        elif mode == "international":
            allowed = reg.get("enabled_countries", []) or []
        self.loader.allowed_regions = set(allowed)

        module_dirs = [
            os.path.join(self.base_dir, "modules", "core_modules"),
            os.path.join(self.base_dir, "modules", "community_modules"),
            os.path.join(self.base_dir, "modules", "user_modules"),
            os.path.join(self.base_dir, "modules", "regional"),
        ]
        self.loader.modules.clear()
        self.loader.scan(module_dirs)
        print("Modules reloaded.")