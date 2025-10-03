# -*- coding: utf-8 -*-
"""
Country (regional) commands for enabling/disabling national modules.
"""
import os
from interface.formatter import Formatter


def _module_directories(project_root: str, enabled_countries=None):
    enabled_countries = set(enabled_countries or [])
    base = os.path.join(project_root, "modules")
    core_dir = os.path.join(base, "core_modules")
    community_dir = os.path.join(base, "community_modules")
    user_dir = os.path.join(base, "user_modules")

    dirs = [
        os.path.join(core_dir, "domain_osint"),
        os.path.join(core_dir, "ip_osint"),
        os.path.join(core_dir, "email_osint"),
        os.path.join(core_dir, "social_media"),
        os.path.join(core_dir, "person_research"),
        os.path.join(core_dir, "corporate_osint"),
        os.path.join(core_dir, "advanced_search"),
        os.path.join(community_dir, "analysis_reporting"),
        os.path.join(community_dir, "visual_osint"),
        os.path.join(community_dir, "integrations"),
        os.path.join(user_dir, "personal_automation"),
        os.path.join(user_dir, "data_processing"),
        os.path.join(user_dir, "integrations"),
        os.path.join(user_dir, "special_targets"),
        os.path.join(user_dir, "personal_reporting"),
        os.path.join(user_dir, "workflows"),
        os.path.join(user_dir, "security_privacy"),
    ]

    # add all enabled regional dirs
    for code in enabled_countries:
        dirs.append(os.path.join(base, "regional", code))

    return dirs


class CountryCommands:
    def __init__(self, loader, cfg, project_root: str):
        self.loader = loader
        self.cfg = cfg
        self.project_root = project_root

    def _get_enabled(self):
        regional = self.cfg.get("regional", {}) or {}
        return list(regional.get("enabled_countries", []))

    def _save_enabled(self, codes):
        data = self.cfg.data or {}
        reg = data.setdefault("regional", {})
        reg["enabled_countries"] = list(sorted(set(codes)))
        self.cfg.data = data
        self.cfg.save()

    def _rescan(self, codes):
        self.loader.modules.clear()
        self.loader.allowed_regions = set(codes)
        self.loader.scan(_module_directories(self.project_root, codes))
        print(Formatter.info(f"Modules reloaded for countries: {', '.join(codes) or '(none)'}"))

    # TR/EN aliases
    def ulke_liste(self, _args=None):
        self.country_list(_args)

    def country_list(self, _args=None):
        codes = self._get_enabled()
        if not codes:
            print(Formatter.info("No countries enabled / Etkin ülke yok"))
            return
        print(Formatter.title("Enabled Countries / Etkin Ülkeler"))
        for c in codes:
            print(f"- {c}")

    def ulke_etkinlestir(self, args):
        self.country_enable(args)

    def country_enable(self, args):
        if not args:
            print(Formatter.error("Usage: country_enable <code> / ulke_etkinlestir <kod>"))
            return
        code = args[0].lower()
        codes = self._get_enabled()
        if code in codes:
            print(Formatter.info(f"Country '{code}' already enabled"))
        else:
            codes.append(code)
            self._save_enabled(codes)
            self._rescan(codes)

    def ulke_devre_disi(self, args):
        self.country_disable(args)

    def country_disable(self, args):
        if not args:
            print(Formatter.error("Usage: country_disable <code> / ulke_devre_disi <kod>"))
            return
        code = args[0].lower()
        codes = [c for c in self._get_enabled() if c != code]
        self._save_enabled(codes)
        self._rescan(codes)

    def ulke_ayarla(self, args):
        self.country_set(args)

    def country_set(self, args):
        if not args:
            print(Formatter.error("Usage: country_set <code> / ulke_ayarla <kod>"))
            return
        codes = [args[0].lower()]
        self._save_enabled(codes)
        self._rescan(codes)

    def modulleri_yeniden_yukle(self, _args=None):
        self.reload_modules(_args)

    def reload_modules(self, _args=None):
        codes = self._get_enabled()
        self._rescan(codes)