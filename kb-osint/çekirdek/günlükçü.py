"""
Günlükçü (logger) sistemi (iskelet).
"""
class Gunlukcu:
    def bilgi(self, mesaj: str):
        print(f"[BILGI] {mesaj}")
    def hata(self, mesaj: str):
        print(f"[HATA] {mesaj}")