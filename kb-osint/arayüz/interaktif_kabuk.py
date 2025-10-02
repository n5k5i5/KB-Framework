# -*- coding: utf-8 -*-
"""
Interactive shell.
"""
from arayüz.komut_işleyici import KomutIsleyici
from arayüz.renklendirici import Renklendirici


class InteraktifKabuk:
    def __init__(self):
        self.prompt = "KB-OSINT> "
        self.komutlar = {}
        self.parser = KomutIsleyici()

    def komut_ekle(self, ad, islev, aciklama=""):
        self.komutlar[ad] = (islev, aciklama)

    def yardim(self):
        print(Renklendirici.title("Available Commands / Kullanılabilir Komutlar"))
        for ad, (_, aciklama) in sorted(self.komutlar.items()):
            print(f"{ad:20} {aciklama}")

    def calistir(self):
        self.yardim()
        while True:
            try:
                satir = input(self.prompt).strip()
            except (EOFError, KeyboardInterrupt):
                print("\n" + Renklendirici.info("Exiting... / Çıkılıyor..."))
                break

            if not satir:
                continue

            parcalar = self.parser.parse(satir)
            komut = parcalar[0]
            args = parcalar[1:]

            if komut in {"cikis", "exit"}:
                print(Renklendirici.info("Exiting... / Çıkılıyor..."))
                break

            if komut in {"yardim", "help"}:
                self.yardim()
                continue

            if komut in self.komutlar:
                islev, _ = self.komutlar[komut]
                try:
                    islev(args)
                except Exception as e:
                    print(Renklendirici.error(f"Command execution error: {e}"))
            else:
                print(Renklendirici.error(f"Unknown command: {komut}. Use 'help' / 'yardim'."))