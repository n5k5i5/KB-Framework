"""XML dışa aktarım (iskelet)."""
def disari(rapor: dict, yol: str) -> bool:
    open(yol, "w", encoding="utf-8").write("<rapor></rapor>")
    return True