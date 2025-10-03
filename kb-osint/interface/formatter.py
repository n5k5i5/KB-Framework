"""
Output formatter (skeletal).
"""
class Formatter:
    # English defaults
    @staticmethod
    def title(m): return f"[TITLE] {m}"
    @staticmethod
    def info(m): return f"[INFO] {m}"
    @staticmethod
    def error(m): return f"[ERROR] {m}"
    @staticmethod
    def emphasis(m): return f"*{m}*"
    @staticmethod
    def highlight(m): return f"> {m} <"

# Turkish aliases (backward compatibility)
class Renklendirici(Formatter):
    @staticmethod
    def baslik(m): return Formatter.title(m)
    @staticmethod
    def bilgi(m): return Formatter.info(m)
    @staticmethod
    def hata(m): return Formatter.error(m)
    @staticmethod
    def vurgu(m): return Formatter.emphasis(m)
    @staticmethod
    def vurgula(m): return Formatter.highlight(m)