# -*- coding: utf-8 -*-
"""
Module commands and CLI integration.
"""
from interface.module_lister import ModuleLister
from interface.formatter import Formatter
from reports.engine import ReportingEngine
from integrations.bus import IntegrationsBus


class ModuleCommands:
    def __init__(self, loader):
        self.loader = loader
        self.lister = ModuleLister()
        self.reporting = ReportingEngine()
        self.bus = IntegrationsBus({})

    # TR/EN aliases supported via registration
    def module_list(self, params=None):
        if not params:
            self.lister.list(self.loader.modules)
            return
        sub = (params[0] or "").lower()

        if sub in {"detayli", "detailed"}:
            self.lister.list(self.loader.modules, detail_level="detayli")
        elif sub in {"kategori", "category"}:
            if len(params) > 1:
                self._list_category(params[1])
            else:
                self._list_categories()
        elif sub in {"ara", "search"}:
            if len(params) > 1:
                self._search(params[1])
            else:
                print(Formatter.error("Arama metni gerekli / search text required: modul_liste|module_list ara|search <metin>"))
        elif sub in {"aktif", "active"}:
            self._list_active()
        elif sub in {"pasif", "inactive"}:
            self._list_inactive()
        else:
            print(Formatter.error("Geçersiz alt komut / invalid subcommand. modul_liste|module_list [detayli|detailed|kategori|category|ara|search|aktif|active|pasif|inactive]"))

    def module_run(self, params=None):
        """
        Run a module with params. Usage:
          module_run <module_name> key=value key2=value2 ...
          modul_calistir <modul_adi> anahtar=deger ...
        """
        if not params:
            print(Formatter.error("Kullanım / Usage: module_run <module_name> key=value ..."))
            return
        name = params[0]
        kvs = params[1:] if len(params) > 1 else []
        args = {}
        for kv in kvs:
            if "=" in kv:
                k, v = kv.split("=", 1)
                args[k.strip()] = v.strip()

        try:
            instance = self.loader.instantiate(name)
        except Exception as e:
            print(Formatter.error(f"Modül çalıştırılamadı / cannot instantiate: {e}"))
            return

        result = {}
        try:
            result = instance.calistir(args)
        except Exception as e:
            print(Formatter.error(f"Çalıştırma hatası / run error: {e}"))
            return

        report = self.reporting.build(f"Module run: {name}", {"params": args}, result, getattr(instance, "metadata", {}))
        json_path = self.reporting.save(report, fmt="json")
        md_path = self.reporting.save(report, fmt="md")

        print(Formatter.info(f"Rapor kaydedildi / Report saved: {json_path}, {md_path}"))
        self.bus.send(["console"], f"Module run: {name}", {"report_json": json_path, "report_md": md_path, "result": result})

    def _list_categories(self):
        categories = self.lister.by_category(self.loader.modules)
        print(Formatter.title("MODÜL KATEGORİLERİ / MODULE CATEGORIES"))
        print("=" * 30)
        for cat, module_list in sorted(categories.items()):
            print(f"📁 {cat}: {len(module_list)} modül")

    def _list_category(self, category: str):
        categories = self.lister.by_category(self.loader.modules)
        if category not in categories:
            available = ", ".join(sorted(categories.keys())) or "(none)"
            print(Formatter.error(f"'{category}' kategorisi bulunamadı / category not found!"))
            print(Formatter.info(f"Mevcut kategoriler / available: {available}"))
            return
        print(Formatter.title(f"{category.upper()} KATEGORİSİ MODÜLLERİ"))
        print("=" * 50)
        for i, (name, module) in enumerate(sorted(categories[category]), 1):
            self.lister._single_module_info(i, name, module, "normal")

    def _search(self, text: str):
        result = self.lister.filter(self.loader.modules, search_text=text)
        if not result:
            print(Formatter.error(f"'{text}' ile eşleşen modül bulunamadı! / no matches"))
            return
        print(Formatter.title(f"'{text}' ARAMA SONUÇLARI / SEARCH RESULTS ({len(result)} modül)"))
        print("=" * 60)
        for i, name in enumerate(sorted(result.keys()), 1):
            self.lister._single_module_info(i, name, result[name], "normal")

    def _list_active(self):
        active = self.lister.filter(self.loader.modules, status=True)
        print(Formatter.title(f"AKTİF / ACTIVE MODÜLLER ({len(active)} modül)"))
        print("=" * 40)
        for i, name in enumerate(sorted(active.keys()), 1):
            self.lister._single_module_info(i, name, active[name], "normal")

    def _list_inactive(self):
        inactive = self.lister.filter(self.loader.modules, status=False)
        if not inactive:
            print(Formatter.info("Pasif modül bulunamadı / no inactive modules"))
            return
        print(Formatter.title(f"PASİF / INACTIVE MODÜLLER ({len(inactive)} modül)"))
        print("=" * 40)
        for i, name in enumerate(sorted(inactive.keys()), 1):
            self.lister._single_module_info(i, name, inactive[name], "normal")