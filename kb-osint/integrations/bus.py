# -*- coding: utf-8 -*-
import json
import logging
from logging.handlers import SysLogHandler
from typing import Dict, Any, Optional, List

try:
    import requests
except Exception:
    requests = None

class IntegrationsBus:
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.logger = logging.getLogger("KB_IntegrationsBus")
        self.logger.setLevel(logging.INFO)

    def send(self,
             targets: List[str],
             title: str,
             payload: Dict[str, Any]) -> Dict[str, Any]:
        result = {}
        for target in targets:
            try:
                if target == "console":
                    print(f"[BUS] {title}\n{json.dumps(payload, ensure_ascii=False, indent=2)}")
                    result[target] = True
                elif target == "file":
                    path = self.config.get("integrations", {}).get("file_path", "kb-osint/reports/outputs.log")
                    with open(path, "a", encoding="utf-8") as f:
                        f.write(json.dumps({"title": title, "payload": payload}, ensure_ascii=False) + "\n")
                    result[target] = True
                elif target == "syslog":
                    host = self.config.get("integrations", {}).get("syslog_host", "localhost")
                    port = int(self.config.get("integrations", {}).get("syslog_port", 514))
                    handler = SysLogHandler(address=(host, port))
                    self.logger.addHandler(handler)
                    self.logger.info(f"{title} {json.dumps(payload, ensure_ascii=False)}")
                    result[target] = True
                elif target == "http_webhook":
                    if not requests:
                        result[target] = False
                    else:
                        url = self.config.get("integrations", {}).get("webhook_url")
                        if not url:
                            result[target] = False
                        else:
                            r = requests.post(url, json={"title": title, "data": payload}, timeout=10)
                            result[target] = (200 <= r.status_code < 300)
                elif target == "slack_webhook":
                    if not requests:
                        result[target] = False
                    else:
                        url = self.config.get("integrations", {}).get("slack_webhook_url")
                        if not url:
                            result[target] = False
                        else:
                            text = f"*{title}*\n```{json.dumps(payload, ensure_ascii=False, indent=2)}```"
                            r = requests.post(url, json={"text": text}, timeout=10)
                            result[target] = (200 <= r.status_code < 300)
                else:
                    result[target] = False
            except Exception as e:
                result[target] = False
                print(f"[BUS] {target} send error: {e}")
        return result