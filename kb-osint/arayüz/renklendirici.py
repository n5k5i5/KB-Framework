"""
Renkli çıktı yardımcıları (iskelet).
"""
class Renklendirici:
    @staticmethod
    def baslik(m): return f"[BASLIK] {m}"
    @staticmethod
    def bilgi(m): return f"[BILGI] {m}"
    @staticmethod
    def hata(m): return f"[HATA] {m}"
    @staticmethod
    def vurgu(m): return f"*{m}*"