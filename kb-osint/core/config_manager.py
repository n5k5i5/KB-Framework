# -*- coding: utf-8 -*-
"""
Central configuration manager (core).
"""
import os
import yaml


class ConfigManager:
    def __init__(self, path="kb-osint/config/main_config.yaml"):
        self.path = path
        self.data = {}

    def load(self):
        if not os.path.exists(self.path):
            self.data = {}
            return
        with open(self.path, "r", encoding="utf-8") as f:
            self.data = yaml.safe_load(f) or {}

    def get(self, key, default=None):
        return self.data.get(key, default)

    def save(self):
        """Write current configuration to YAML file."""
        folder = os.path.dirname(self.path)
        if folder and not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
        with open(self.path, "w", encoding="utf-8") as f:
            yaml.safe_dump(self.data or {}, f, allow_unicode=True, sort_keys=False)