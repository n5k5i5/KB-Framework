"""
Komut satırı arayüzü (iskelet).
"""
class CLI:
    def __init__(self):
        self.komutlar = {}

    def komut_ekle(self, ad, fonk, aciklama=""):
        self.komutlar[ad] = (fonk, aciklama)

    def calistir(self):
        pass