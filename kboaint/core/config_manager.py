# -*- coding: utf-8 -*-
import os
from typing import Any, Dict

try:
    import yaml
except Exception:
    yaml = None

class ConfigManager:
    def __init__(self, path: str):
        self.path = path
        self.data: Dict[str, Any] = {}
        self.load()

    def load(self) -> None:
        if not os.path.isfile(self.path):
            # default minimal config
            self.data = {
                "system": {"language": "en", "log_level": "info"},
                "regional": {"mode": "international", "enabled_countries": []},
                "reporting": {"output_dir": "./reports", "default_format": "json"},
            }
            return
        try:
            if yaml:
                with open(self.path, "r", encoding="utf-8") as f:
                    self.data = yaml.safe_load(f) or {}
            else:
                # naive parser
                self.data = {}
        except Exception:
            self.data = {}

    def save(self) -> None:
        if yaml:
            try:
                with open(self.path, "w", encoding="utf-8") as f:
                    yaml.safe_dump(self.data, f, allow_unicode=True, sort_keys=False)
            except Exception:
                pass

    def get(self, key: str, default=None):
        return self.data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self.data[key] = value