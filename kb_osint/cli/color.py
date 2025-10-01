class KB_Renklendirici:
    RENKLER = {
        "BASLIK": "\033[95m",
        "BASARILI": "\033[92m",
        "UYARI": "\033[93m",
        "HATA": "\033[91m",
        "BILGI": "\033[94m",
        "VURGU": "\033[96m",
        "NORMAL": "\033[0m",
    }

    @classmethod
    def baslik(cls, metin: str) -> str:
        return f"{cls.RENKLER['BASLIK']}{metin}{cls.RENKLER['NORMAL']}"

    @classmethod
    def basarili(cls, metin: str) -> str:
        return f"{cls.RENKLER['BASARILI']}✓ {metin}{cls.RENKLER['NORMAL']}"

    @classmethod
    def hata(cls, metin: str) -> str:
        return f"{cls.RENKLER['HATA']}✗ {metin}{cls.RENKLER['NORMAL']}"

    @classmethod
    def bilgi(cls, metin: str) -> str:
        return f"{cls.RENKLER['BILGI']}ℹ {metin}{cls.RENKLER['NORMAL']}"