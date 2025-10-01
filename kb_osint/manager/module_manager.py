import os
import importlib.util
from typing import Dict, Any, Optional

from kb_osint.core.interface import KB_Modul_Arayuzu


class KB_Modul_Yoneticisi:
    """
    Modül yöneticisi: modül keşfi, yükleme ve kayıt işlemleri (iskelet).
    """

    def __init__(self):
        self.moduller: Dict[str, Any] = {}
        self.modul_dizinleri = [
            "./moduller/cekirdek_moduller",
            "./moduller/topluluk_modulleri",
            "./moduller/kullanici_modulleri",
        ]

    def modul_tara(self) -> None:
        """Tüm modül dizinlerini tarar ve yükler."""
        for dizin in self.modul_dizinleri:
            if not os.path.isdir(dizin):
                continue
            for dosya in os.listdir(dizin):
                if dosya.startswith("kb_") and dosya.endswith(".py"):
                    yol = os.path.join(dizin, dosya)
                    self.modul_yukle(yol)

    def modul_yukle(self, modul_dosyasi: str) -> Optional[str]:
        """Tek modül yükler ve kayıt eder."""
        try:
            spec = importlib.util.spec_from_file_location("kb_modul", modul_dosyasi)
            modul = importlib.util.module_from_spec(spec)
            assert spec and spec.loader, "Yükleme spesifikasyonu bulunamadı"
            spec.loader.exec_module(modul)

            # 1) Arayüzü implement eden sınıfı bul
            for attr_name in dir(modul):
                attr = getattr(modul, attr_name)
                if isinstance(attr, type) and issubclass(attr, KB_Modul_Arayuzu) and attr is not KB_Modul_Arayuzu:
                    ornek = attr()
                    modul_adi = ornek.metadata.get("modul_adi") or os.path.basename(modul_dosyasi).replace(".py", "")
                    self.moduller[modul_adi] = ornek
                    return modul_adi

            # 2) MANIFEST ile kayıt (iskele modüller için)
            if hasattr(modul, "MANIFEST") and isinstance(modul.MANIFEST, dict):
                modul_adi = modul.MANIFEST.get("modul_adi") or os.path.basename(modul_dosyasi).replace(".py", "")
                self.moduller[modul_adi] = modul.MANIFEST
                return modul_adi

        except Exception as e:
            print(f"Modül yükleme hatası ({modul_dosyasi}): {e}")
        return None

    def listele(self) -> Dict[str, Any]:
        """Yüklü modülleri döndürür."""
        return self.moduller.copy()