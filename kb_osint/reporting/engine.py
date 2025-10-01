from typing import Dict, Any


class KB_RaporlamaMotoru:
    """
    Standart rapor şeması ve çıktı üretimi için iskelet sınıf.
    """

    def __init__(self, cikti_klasoru: str = "./raporlar"):
        self.cikti_klasoru = cikti_klasoru

    def rapor_olustur(self, hedef: str, kullanilan_moduller: list, bulgular: Dict[str, Any], istatistikler: Dict[str, Any]) -> Dict[str, Any]:
        """
        Standart rapor sözlüğü döndürür (JSON uyumlu).
        """
        return {
            "rapor_meta": {
                "kb_versiyon": "1.0.0",
                "hedef": hedef,
                "kullanilan_moduller": kullanilan_moduller,
            },
            "bulgular": bulgular,
            "istatistikler": istatistikler,
        }