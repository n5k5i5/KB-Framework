"""
Modül listeleyici (iskelet).
"""
class ModulLister:
    def listele(self, moduller: dict):
        for i, (ad, meta) in enumerate(sorted(moduller.items()), 1):
            print(f"{i:2d}. {ad} - {meta.get('aciklama', '')}")