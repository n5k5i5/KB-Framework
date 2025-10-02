"""
Output formatter (skeletal).
"""
class Renklendirici:
    # Turkish aliases (backward compatibility)
    @staticmethod
    def baslik(m): return f"[TITLE] {m}"
    @staticmethod
    def bilgi(m): return f"[INFO] {m}"
    @staticmethod
    def hata(m): return f"[ERROR] {m}"
    @staticmethod
    def vurgu(m): return f"*{m}*"

    # English defaults
    @staticmethod
    def title(m): return f"[TITLE] {m}"
    @staticmethod
    def info(m): return f"[INFO] {m}"
    @staticmethod
    def error(m): return f"[ERROR] {m}"
    @staticmethod
    def emphasis(m): return f"*{m}*"