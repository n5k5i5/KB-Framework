"""
Format dönüştürücü (iskelet).
"""
def to_json(veri: dict) -> str:
    import json
    return json.dumps(veri, ensure_ascii=False)