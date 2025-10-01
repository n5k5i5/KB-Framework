import hashlib
from typing import Dict, List


class KB_Guvenlik_Yoneticisi:
    """
    İmza doğrulama ve basit güvenlik taraması (iskelet).
    """

    def __init__(self):
        self.imza_veritabani: Dict[str, Dict[str, str]] = {
            "resmi_moduller": {
                "kb_domain": "KB_IMZA_XYZ123",
                "kb_ip": "KB_IMZA_ABC456",
            },
            "onayli_gelistiriciler": {
                "developer1": "GELISTIRICI_IMZA_789",
            },
        }

    def modul_imzala(self, modul_dosyasi: str) -> str:
        """Modülü dijital olarak imzalar (SHA-256 hash)."""
        with open(modul_dosyasi, "rb") as f:
            icerik = f.read()
        imza = hashlib.sha256(icerik).hexdigest()
        return f"KB_MODUL_{imza}"

    def modul_dogrula(self, modul_adi: str, imza: str) -> bool:
        """Modül imzasını doğrular (resmi kayıtlıysa)."""
        resmi = self.imza_veritabani.get("resmi_moduller", {})
        kayitli = resmi.get(modul_adi)
        return kayitli == imza if kayitli else False

    def guvenlik_taramasi(self, modul_kodu: str) -> Dict[str, List[str] or str]:
        """Basit statik tarama; tehlikeli fonksiyonları yakalar."""
        tehlikeli = [
            "eval", "exec", "compile", "__import__", "open",
            "os.system", "subprocess.call", "popen",
        ]
        tespit: List[str] = [fn for fn in tehlikeli if fn in modul_kodu]
        seviye = "yuksek" if tespit else "dusuk"
        oneriler: List[str] = ["Modül yüksek risk içeriyor"] if tespit else []
        return {
            "risk_seviyesi": seviye,
            "tespit_edilen_riskler": tespit,
            "oneriler": oneriler,
        }