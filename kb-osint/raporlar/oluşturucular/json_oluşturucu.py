"""JSON rapor oluşturucu (iskelet)."""
import json
def olustur(rapor: dict) -> str:
    return json.dumps(rapor, ensure_ascii=False, indent=2)