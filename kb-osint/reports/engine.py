# -*- coding: utf-8 -*-
import os
import json
from datetime import datetime
from typing import Dict, Any, Optional

class ReportingEngine:
    def __init__(self, output_dir: str = "kb-osint/reports"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def build(self,
              title: str,
              input_data: Dict[str, Any],
              result: Dict[str, Any],
              metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return {
            "title": title,
            "time": datetime.utcnow().isoformat() + "Z",
            "input": input_data,
            "result": result,
            "metadata": metadata or {},
        }

    def to_json(self, report: Dict[str, Any]) -> str:
        return json.dumps(report, ensure_ascii=False, indent=2)

    def to_markdown(self, report: Dict[str, Any]) -> str:
        lines = []
        lines.append(f"# {report.get('title','Report')}")
        lines.append(f"- Time: {report.get('time','')}")
        lines.append("## Input")
        lines.append("```json")
        lines.append(json.dumps(report.get('input', {}), ensure_ascii=False, indent=2))
        lines.append("```")
        lines.append("## Result")
        lines.append("```json")
        lines.append(json.dumps(report.get('result', {}), ensure_ascii=False, indent=2))
        lines.append("```")
        lines.append("## Metadata")
        lines.append("```json")
        lines.append(json.dumps(report.get('metadata', {}), ensure_ascii=False, indent=2))
        lines.append("```")
        return "\n".join(lines)

    def to_html(self, report: Dict[str, Any]) -> str:
        def esc(s: str) -> str:
            return s.replace("&","&amp;").replac("<","&lt;").replace(">","&gt;")
        return f"""<!doctype html>
<html><head><meta charset="utf-8"><title>{esc(report.get('title','Report')}</title>
<style>body{{font-family:Arial,Helvetica,sans-serif;margin:20px}}pre{{background:#f6f8fa;padding:10px;border:1