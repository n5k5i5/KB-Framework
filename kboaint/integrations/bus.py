# -*- coding: utf-8 -*-
from typing import Dict, Any

class IntegrationsBus:
    def send(self, channel: str, payload: Dict[str, Any]) -> bool:
        # Placeholder: always succeeds
        print(f"[bus:{channel}] {payload}")
        return True