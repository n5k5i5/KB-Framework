"""
API yöneticisi (iskelet).
"""
class APIYoneticisi:
    def sorgu(self, servis: str, param: dict):
        return {"servis": servis, "sonuc": None}