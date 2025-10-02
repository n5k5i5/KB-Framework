# -*- coding: utf-8 -*-
"""
Country (regional) commands for enabling/disabling national modules.
"""
import os
from arayüz.renklendirici import Renklendirici


def _modul_dizinleri(proje_kok: str, enabled_countries=None):
    enabled_countries = set(enabled_countries or [])
    base = os.path.join(proje_kok, "modüller")
    cekirdek = os.path.join(base, "çekirdek_modüller")
    topluluk = os.path.join(base, "topluluk_modülleri")
    kullanici = os.path.join(base, "kullanıcı_modülleri")

    dizinler = [
        os.path.join(cekirdek, "domain_osint"),
        os.path.join(cekirdek, "ip_osint"),
        os.path.join(cekirdek, "email_osint"),
        os.path.join(cekirdek, "sosyal_medya"),
        os.path.join(cekirdek, "kişi_araştırma"),
        os.path.join(cekirdek, "kurumsal_osint"),
        os.path.join(cekirdek, "gelişmiş_arama"),
        os.path.join(topluluk, "analiz_raporlama"),
        os.path.join(topluluk, "görsel_osint"),
        os.path.join(topluluk, "entegrasyonlar"),
        os.path.join(kullanici, "kişisel_otomasyon"),
        os.path.join(kullanici, "veri_işleme"),
        os.path.join(kullanici, "entegrasyonlar"),
        os.path.join(kullanici, "özel_hedefler"),
        os.path.join(kullanici, "kişisel_raporlama"),
        os.path.join(kullanici, "iş_akışı"),
        os.path.join(kullanici, "güvenlik_gizlilik"),
    ]

    # add all enabled regional dirs
    for code in enabled_countries:
        dizinler.append(os.path.join(base, "regional", code))

    return dizinler


class UlkeKomutlari:
    def __init__(self, yukleyici, cfg, proje_kok: str):
        self.y = yukleyici
        self.cfg = cfg
        self.proje_kok = proje_kok

    def _get_enabled(self):
        regional = self.cfg.al("regional", {}) or {}
        return list(regional.get("enabled_countries", []))

    def _save_enabled(self, codes):
        data = self.cfg.veri or {}
        reg = data.setdefault("regional", {})
        reg["enabled_countries"] = list(sorted(set(codes)))
        self.cfg.veri = data
        self.cfg.kaydet()

    def _rescan(self, codes):
        self.y.moduller.clear()
        self.y.allowed_regions = set(codes)
        self.y.tara(_modul_dizinleri(self.proje_kok, codes))
        print(Renklendirici.info(f"Modules reloaded for countries: {', '.join(codes) or '(none)'}"))

    # TR/EN aliases
    def ulke_liste(self, _args=None):
        self.country_list(_args)

    def country_list(self, _args=None):
        codes = self._get_enabled()
        if not codes:
            print(Renklendirici.info("No countries enabled / Etkin ülke yok"))
            return
        print(Renklendirici.title("Enabled Countries / Etkin Ülkeler"))
        for c in codes:
            print(f"- {c}")

    def ulke_etkinlestir(self, args):
        self.country_enable(args)

    def country_enable(self, args):
        if not args:
            print(Renklendirici.error("Usage: country_enable <code> / ulke_etkinlestir <kod>"))
            return
        code = args[0].lower()
        codes = self._get_enabled()
        if code in codes:
            print(Renklendirici.info(f"Country '{code}' already enabled"))
        else:
            codes.append(code)
            self._save_enabled(codes)
            self._rescan(codes)

    def ulke_devre_disi(self, args):
        self.country_disable(args)

    def country_disable(self, args):
        if not args:
            print(Renklendirici.error("Usage: country_disable <code> / ulke_devre_disi <kod>"))
            return
        code = args[0].lower()
        codes = [c for c in self._get_enabled() if c != code]
        self._save_enabled(codes)
        self._rescan(codes)

    def ulke_ayarla(self, args):
        self.country_set(args)

    def country_set(self, args):
        if not args:
            print(Renklendirici.error("Usage: country_set <code> / ulke_ayarla <kod>"))
            return
        codes = [args[0].lower()]
        self._save_enabled(codes)
        self._rescan(codes)

    def modulleri_yeniden_yukle(self, _args=None):
        self.reload_modules(_args)

    def reload_modules(self, _args=None):
        codes = self._get_enabled()
        self._rescan(codes)