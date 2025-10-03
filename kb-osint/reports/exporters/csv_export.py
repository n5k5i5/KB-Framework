"""CSV dışa aktarım (iskelet)."""
def disari(rapor: dict, yol: str) -> bool:
    open(yol, "w", encoding="utf-8").write("csv,icerik,yer,tutucu\n")
    return True