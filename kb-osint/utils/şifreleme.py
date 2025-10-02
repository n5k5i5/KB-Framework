"""
Şifreleme yardımcıları (iskelet).
"""
def hash_str(veri: str) -> str:
    import hashlib
    return hashlib.sha256(veri.encode("utf-8")).hexdigest()