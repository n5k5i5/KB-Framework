"""Excel dışa aktarım (iskelet)."""
def disari(rapor: dict, yol: str) -> bool:
    # İskelet: gerçek XLSX yazımı yok
    open(yol, "w", encoding="utf-8").write("EXCEL RAPOR Y