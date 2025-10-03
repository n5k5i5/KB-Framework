"""
Rapor yöneticisi (iskelet).
"""
class RaporYoneticisi:
    def olustur(self, tip: str, veri: dict) -> dict:
        return {"rapor_tipi": tip, "veri": veri}