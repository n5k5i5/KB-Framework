"""Markdown rapor oluşturucu (iskelet)."""
def olustur(rapor: dict) -> str:
    baslik = f"# Rapor - {rapor.get('rapor_tipi', 'Genel')}"
    return baslik + "\n\n" + str(rapor)