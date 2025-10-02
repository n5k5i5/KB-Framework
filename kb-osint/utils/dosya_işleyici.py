"""
Dosya işleyici (iskelet).
"""
def oku(yol: str) -> str:
    try:
        with open(yol, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""