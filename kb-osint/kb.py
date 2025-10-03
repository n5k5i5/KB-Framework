"""
KB-OSINT main application (skeleton).
"""
import os
from interface.interactive_shell import InteractiveShell
from core.loader import Loader
from core.config_manager import ConfigManager
from interface.module_commands import ModuleCommands
from interface.country_commands import CountryCommands


def _module_directories(project_root: str, enabled_countries=None):
    enabled_countries = set(enabled_countries or [])
    base = os.path.join(project_root, "modules")
    core_dir = os.path.join(base, "core_modules")
    community_dir = os.path.join(base, "community_modules")
    user_dir = os.path.join(base, "user_modules")

    dirs = [
        # Core
        os.path.join(core_dir, "domain_osint"),
        os.path.join(core_dir, "ip_osint"),
        os.path.join(core_dir, "email_osint"),
        os.path.join(core_dir, "social_media"),
        os.path.join(core_dir, "person_research"),
        os.path.join(core_dir, "corporate_osint"),
        os.path.join(core_dir, "advanced_search"),
        # Community
        os.path.join(community_dir, "analysis_reporting"),
        os.path.join(community_dir, "visual_osint"),
        os.path.join(community_dir, "integrations"),
        # User
        os.path.join(user_dir, "personal_automation"),
        os.path.join(user_dir, "data_processing"),
        os.path.join(user_dir, "integrations"),
        os.path.join(user_dir, "special_targets"),
        os.path.join(user_dir, "personal_reporting"),
        os.path.join(user_dir, "workflows"),
        os.path.join(user_dir, "security_privacy"),
    ]

    # Regional (country) modules
    for code in enabled_countries:
        dirs.append(os.path.join(base, "regional", code))

    return dirs


def main():
    project_root = os.path.dirname(__file__)

    # Load config and regional settings
    cfg = ConfigManager()
    cfg.load()
    regional = cfg.get("regional", {}) or {}
    mode = regional.get("mode", "international")
    country_code = regional.get("country_code") or ""
    enabled_countries = regional.get("enabled_countries", [])
    if mode == "national" and country_code:
        enabled_countries = [country_code]

    loader = Loader(allowed_regions=enabled_countries)
    loader.scan(_module_directories(project_root, enabled_countries))

    shell = InteractiveShell()
    mk = ModuleCommands(loader)
    uk = CountryCommands(loader, cfg, project_root)

    # Commands (TR and EN aliases)
    shell.register_command("modul_liste", mk.module_list, "Modülleri listeler - modul_liste [detayli|kategori|ara|aktif|pasif]")
    shell.register_command("module_list", mk.module_list, "List modules - module_list [detailed|category|search|active|inactive]")
    shell.register_command("modul_kategoriler", lambda *_: mk._list_categories(), "Tüm modül kategorilerini listeler")
    shell.register_command("module_categories", lambda *_: mk._list_categories(), "List all module categories")
    shell.register_command("modul_ara", lambda args: mk._search(args[0] if args else ""), "Modüllerde arama yapar - modul_ara <metin>")
    shell.register_command("module_search", lambda args: mk._search(args[0] if args else ""), "Search modules - module_search <text>")

    # Run module
    shell.register_command("modul_calistir", mk.module_run, "Modül çalıştır - modul_calistir <modul_adi> anahtar=deger ...")
    shell.register_command("module_run", mk.module_run, "Run module - module_run <module_name> key=value ...")

    # Country (regional) commands
    shell.register_command("ulke_liste", uk.country_list, "Etkin ülkeleri listeler / List enabled countries")
    shell.register_command("country_list", uk.country_list, "List enabled countries")
    shell.register_command("ulke_etkinlestir", uk.country_enable, "Ülke etkinleştir / Enable country: ulke_etkinlestir <kod>")
    shell.register_command("country_enable", uk.country_enable, "Enable country: country_enable <code>")
    shell.register_command("ulke_devre_disi", uk.country_disable, "Ülke devre dışı / Disable country: ulke_devre_disi <kod>")
    shell.register_command("country_disable", uk.country_disable, "Disable country: country_disable <code>")
    shell.register_command("ulke_ayarla", uk.country_set, "Tek ülke modu / National: ulke_ayarla <kod>")
    shell.register_command("country_set", uk.country_set, "National mode: country_set <code>")
    shell.register_command("modulleri_yeniden_yukle", uk.reload_modules, "Modülleri yeniden yükle / Reload modules")
    shell.register_command("reload_modules", uk.reload_modules, "Reload modules")

    # Built-ins (TR and EN)
    shell.register_command("yardim", lambda *_: shell.help(), "Yardım metnini gösterir")
    shell.register_command("help", lambda *_: shell.help(), "Show help")
    shell.register_command("cikis", lambda *_: None, "Kabuğu kapatır")
    shell.register_command("exit", lambda *_: None, "Exit shell")

    shell.run()


if __name__ == "__main__":
    main()