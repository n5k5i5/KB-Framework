"""
Interaktif kabuk (iskelet).
"""
class InteraktifKabuk:
    def __init__(self):
        self.prompt = "KB-OSINT> "
        self.komutlar = {}

    def komut_ekle(self, ad, islev, aciklama=""):
        self.komutlar[ad] = (islev, aciklama)

    def yardim(self):
        for ad, (_, aciklama) in sorted(self.komutlar.items()):
            print(f"{ad:20} {aciklama}")

    def calistir(self):
        # İskelet: gerçek döngü implement edilmedi
        self.yardim()