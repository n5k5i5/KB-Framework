# -*- coding: utf-8 -*-
from typing import List, Dict, Any

from kboaint.core.loader import Loader
from kboaint.core.interface import KB_Modul_Arayuzu

class ModuleCommands:
    def __init__(self, loader: Loader):
        self.loader = loader

    def module_list(self, args: List[str]) -> None:
        mods = self.loader.list()
        if not mods:
            print("No modules loaded.")
            return
        mode = "normal"
        if args:
            if args[0] in {"detayli", "detailed"}:
                mode = "detailed"
        print(f"Loaded modules: {len(mods)}")
        for name in sorted(mods.keys()):
            m = mods[name]
            meta = self._meta_of(m)
            print(f"- {name} [{meta.get('kategori','genel')}] - {meta.get('aciklama','')}")
            if mode == "detailed":
                print(f"  version: {meta.get('versiyon') or meta.get('surum','')}")
                print(f"  author : {meta.get('yazar','')}")
                print(f"  active : {meta.get('aktif', True)}")
                print(f"  security: {meta.get('guvenlik_seviyesi','')}")
                apis = ", ".join(meta.get('api_gereksinimleri', [])) or "(none)"
                deps = ", ".join(meta.get('bagimliliklar', [])) or "(none)"
                print(f"  apis   : {apis}")
                print(f"  deps   : {deps}")

    def list_categories(self, _args=None) -> None:
        cats: Dict[str, int] = {}
        for name, m in self.loader.list().items():
            meta = self._meta_of(m)
            c = meta.get("kategori", "genel")
            cats[c] = cats.get(c, 0) + 1
        print("Categories:")
        for c in sorted(cats.keys()):
            print(f"  {c}: {cats[c]}")

    def search(self, args: List[str]) -> None:
        term = (args[0] if args else "").lower()
        if not term:
            print("Usage: module_search <text>")
            return
        found = []
        for name, m in self.loader.list().items():
            meta = self._meta_of(m)
            if term in name.lower() or term in meta.get("aciklama","").lower():
                found.append(name)
        if not found:
            print("No match.")
            return
        print(f"Found ({len(found)}):")
        for n in sorted(found):
            print(f"  - {n}")

    def module_run(self, args: List[str]) -> None:
        if not args:
            print("Usage: module_run <module_name> key=value ...")
            return
        name = args[0]
        kwargs: Dict[str, Any] = {}
        for tok in args[1:]:
            if "=" in tok:
                k, v = tok.split("=", 1)
                kwargs[k] = v
        mods = self.loader.list()
        if name not in mods:
            print(f"Module not found: {name}")
            return
        m = mods[name]
        if isinstance(m, KB_Modul_Arayuzu):
            res = m.calistir(kwargs)
        elif isinstance(m, dict):
            print("Module has no executable class (manifest-only).")
            return
        else:
            print("Invalid module type.")
            return
        print("Result:")
        print(res)

    def _meta_of(self, m: Any) -> Dict[str, Any]:
        if isinstance(m, KB_Modul_Arayuzu):
            return getattr(m, "metadata", {})
        elif isinstance(m, dict):
            return m
        return {}