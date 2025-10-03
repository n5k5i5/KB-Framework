# -*- coding: utf-8 -*-
import os
import sys

BASE_DIR = os.path.dirname(__file__)
sys.path.insert(0, BASE_DIR)

from kboaint.core.config_manager import ConfigManager
from kboaint.core.loader import Loader
from kboaint.interface.interactive_shell import InteractiveShell
from kboaint.interface.module_commands import ModuleCommands
from kboaint.interface.country_commands import CountryCommands

def app():
    cfg_path = os.path.join(BASE_DIR, "config", "main_config.yaml")
    cfg = ConfigManager(cfg_path)

    regional = cfg.get("regional", {}) or {}
    mode = regional.get("mode", "international")
    allowed = []
    if mode == "national" and regional.get("country_code"):
        allowed = [regional["country_code"]]
    elif mode == "international":
        allowed = regional.get("enabled_countries", []) or []

    loader = Loader(allowed_regions=allowed)
    module_dirs = [
        os.path.join(BASE_DIR, "modules", "core_modules"),
        os.path.join(BASE_DIR, "modules", "community_modules"),
        os.path.join(BASE_DIR, "modules", "user_modules"),
        os.path.join(BASE_DIR, "modules", "regional"),
    ]
    loader.scan(module_dirs)

    shell = InteractiveShell()
    mc = ModuleCommands(loader)
    cc = CountryCommands(loader, cfg, BASE_DIR)

    shell.register_command("module_list", mc.module_list, "List modules - module_list [detailed|category|search|active|inactive]")
    shell.register_command("modul_liste", mc.module_list, "Modülleri listeler - modul_liste [detayli|kategori|ara|aktif|pasif]")
    shell.register_command("module_run", mc.module_run, "Run module - module_run <module_name> key=value ...")
    shell.register_command("modul_calistir", mc.module_run, "Modül çalıştır - modul_calistir <modul_adi> anahtar=deger ...")
    shell.register_command("module_categories", mc.list_categories, "List module categories")
    shell.register_command("modul_kategoriler", mc.list_categories, "Modül kategorilerini listeler")
    shell.register_command("module_search", mc.search, "Search modules - module_search <text>")
    shell.register_command("modul_ara", mc.search, "Modüllerde arama - modul_ara <metin>")

    shell.register_command("country_list", cc.country_list, "List enabled countries")
    shell.register_command("ulke_liste", cc.country_list, "Etkin ülkeleri listeler")
    shell.register_command("country_enable", cc.country_enable, "Enable country: country_enable <code>")
    shell.register_command("ulke_etkinlestir", cc.country_enable, "Ülke etkinleştir: ulke_etkinlestir <kod>")
    shell.register_command("country_disable", cc.country_disable, "Disable country: country_disable <code>")
    shell.register_command("ulke_devre_disi", cc.country_disable, "Ülke devre dışı: ulke_devre_disi <kod>")
    shell.register_command("country_set", cc.country_set, "National mode: country_set <code>")
    shell.register_command("ulke_ayarla", cc.country_set, "Tek ülke modu: ulke_ayarla <kod>")
    shell.register_command("reload_modules", cc.reload_modules, "Reload modules")
    shell.register_command("modulleri_yeniden_yukle", cc.reload_modules, "Modülleri yeniden yükle")

    shell.register_command("help", lambda *_: shell.help(), "Show help")
    shell.register_command("yardim", lambda *_: shell.help(), "Yardım")
    shell.register_command("exit", lambda *_: None, "Exit shell")
    shell.register_command("cikis", lambda *_: None, "Çıkış")

    shell.run()

if __name__ == "__main__":
    app()