# -*- coding: utf-8 -*-
"""
Central configuration manager (core).
"""
import os
from typing import Any, Dict, Optional

try:
    import yaml  # optional dependency
except Exception:
    yaml = None


class ConfigManager:
    def __init__(self, path: Optional[str] = None):
        # Default to main_config.yaml for consistency with README
        self.path = path or "kb-osint/config/main_config.yaml"
        self._data: Dict[str, Any] = {}

    def load(self) -> None:
        if not os.path.exists(self.path):
            # minimal defaults
            self._data = {
                "system": {"language": "en", "log_level": "info"},
                "regional": {"mode": "international", "country_code": "", "enabled_countries": []},
            }
            return
        try:
            if yaml:
                with open(self.path, "r", encoding="utf-8") as f:
                    self._data = yaml.safe_load(f) or {}
            else:
                import json
                with open(self.path, "r", encoding="utf-8") as f:
                    self._data = json.loads(f.read())
        except Exception:
            self._data = {
                "system": {"language": "en", "log_level": "info"},
                "regional": {"mode": "international", "country_code": "", "enabled_countries": []},
            }

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self._data[key] = value

    @property
    def data(self) -> Dict[str, Any]:
        return self._data

    def save(self) -> None:
        """Write current configuration to YAML/JSON file."""
        folder = os.path.dirname(self.path)
        if folder and not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
        if yaml:
            with open(self.path, "w", encoding="utf-8") as f:
                yaml.safe_dump(self._data or {}, f, allow_unicode=True, sort_keys=False)
        else:
            import json
            with open(self.path, "w", encoding="utf-8") as f:
                f.write(json.dumps(self._data or {}, ensure_ascii=False, indent=2))