# -*- coding: utf-8 -*-
import os
import json
from typing import Dict, Any

class ReportingEngine:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def save_json(self, name: str, data: Dict[str, Any]) -> str:
        path = os.path.join(self.output_dir, f"{name}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return path