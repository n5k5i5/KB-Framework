# -*- coding: utf-8 -*-
from typing import Dict, Any, Optional

class KB_Modul_Arayuzu:
    metadata: Dict[str, Any] = {
        "modul_adi": "kb_modul",
        "aciklama": "Taban modül",
        "kategori": "cekirdek",
        "surum": "0.1.0",
        "aktif": True,
        "izinler": [],
        "guvenlik_seviyesi": "orta",
        "api_gereksinimleri": [],
        "regional": None,
    }

    def __init__(self,
                 config: Optional[Dict[str, Any]] = None):
        self.config = config or {}

    def dogrula_parametreler(self, params: Dict[str, Any]) -> None:
        if not isinstance(params, dict):
            raise ValueError("Parametreler dict olmalı")

    def calistir(self, params: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError("Modül 'calistir' metodunu uygulamalı.")

    def log(self, mesaj: str) -> None:
        print(f"[{self.metadata.get('modul_adi','kb_modul')}] {mesaj}")