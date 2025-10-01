from typing import Callable, Dict, List
from kb_osint.cli.color import KB_Renklendirici


class KB_Interaktif_Kabuk:
    def __init__(self):
        self.prompt = "KB-OSINT> "
        self.komutlar: Dict[str, Dict[str, Callable]] = {}
        self.gecmis: List[str] = []

    def komut_ekle(self, komut_adi: str, islev: Callable, aciklama: str) -> None:
        self.komutlar[komut_adi] = {
            "islev": islev,
            "aciklama": aciklama,
        }

    def yardim(self) -> None:
        print(KB_Renklendirici.baslik("Kullanılabilir komutlar:"))
        for k, v in sorted(self.komutlar.items()):
            print(f"  - {k:16} {v['aciklama']}")

    def calistir(self) -> None:
        print(KB_Renklendirici.baslik("KB-OSINT Interaktif Kabuğa Hoş Geldiniz"))
        print("yardim komutu ile tüm komutları görebilirsiniz. cikis ile çıkabilirsiniz.")
        while True:
            try:
                girdi = input(self.prompt).strip()
                if not girdi:
                    continue
                self.gecmis.append(girdi)
                parcalar = girdi.split()
                komut = parcalar[0]
                args = parcalar[1:]
                if komut in {"cikis", "exit", "quit"}:
                    print(KB_Renklendirici.bilgi("Güle güle!"))
                    break
                elif komut == "yardim":
                    self.yardim()
                elif komut in self.komutlar:
                    self.komutlar[komut]["islev"](args)
                else:
                    print(KB_Renklendirici.hata(f"Bilinmeyen komut: {komut}"))
            except KeyboardInterrupt:
                print("\n" + KB_Renklendirici.bilgi("Çıkılıyor..."))
                break
            except Exception as e:
                print(KB_Renklendirici.hata(f"Hata: {e}"))