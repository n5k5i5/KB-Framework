"""PDF rapor oluşturucu (iskelet)."""
def olustur(rapor: dict) -> bytes:
    icerik = f"PDF RAPOR\n{rapor}"
    return icerik.encode("utf-8")