"""
KB-OSINT CLI giriş noktası (iskelet).
"""
from arayüz.interaktif_kabuk import InteraktifKabuk

def run():
    shell = InteraktifKabuk()
    shell.calistir()

if __name__ == "__main__":
    run()