"""HTML rapor oluşturucu (iskelet)."""
def olustur(rapor: dict) -> str:
    return "<html><body><pre>" + str(rapor) + "</pre></body></html>"