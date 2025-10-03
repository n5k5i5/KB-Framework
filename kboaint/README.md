# KB-OSINT (single-folder scaffold)

Quick start
- Install: `pip install -r kboaint/requirements.txt`
- Run: `python -m kboaint` (or `python kboaint/main.py`)

Shell commands
- module_list [detailed|detayli|category|kategori|search|ara|active|inactive]
- module_run <module_name> key=value ...
- module_categories / modul_kategoriler
- module_search <text> / modul_ara <metin>
- country_list / ulke_liste
- country_enable <code> / ulke_etkinlestir <kod>
- country_disable <code> / ulke_devre_disi <kod>
- country_set <code> / ulke_ayarla <kod>
- reload_modules / modulleri_yeniden_yukle

Examples
- `module_run kb_domain_whois domain=example.com`
- `module_run kb_domain_dns domain=example.com`
- `module_run kb_ip_geo ip=8.8.8.8`
- `module_run kb_email_verify email=test@example.com`