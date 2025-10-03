# KB-OSINT

Extensible, modular OSINT platform with interactive CLI, regional filtering, and a clear directory layout.

## Quick Start

1) Requirements
- Python 3.10+ recommended
- pip, virtualenv (optional)

2) Install
```
# clone or download the repo, then:
pip install -r kb-osint/requirements.txt
```

3) Configure
- Edit `kb-osint/config/main_config.yaml`:
  ```yaml
  system:
    language: en       # en | tr | ru
    log_level: info

  regional:
    mode: international        # international | national
    country_code: ""           # e.g., "tr" when mode=national
    enabled_countries: []      # e.g., ["tr", "us"] when mode=international
  ```
- Optional API keys: `kb-osint/config/api_keys.yaml`
  ```
  shodan_api_key: ""
  virustotal_api_key: ""
  censys_api_id: ""
  censys_api_secret: ""
  ```

4) Run
```
python kb-osint/kb.py
```
- Use the interactive shell to list modules and run commands.
- Built-in help: type `help` (or `yardim`)

## Usage

Core module commands
- List all modules:
  - `module_list`
  - Turkish alias: `modul_liste`
- Detailed list:
  - `module_list detailed`
  - `modul_liste detayli`
- List by category:
  - `module_list category <category>`
  - `modul_liste kategori <kategori>`
- Search modules:
  - `module_search <text>`
  - `modul_ara <metin>`
- Filter by status:
  - `module_list active` / `module_list inactive`
  - `modul_liste aktif` / `modul_liste pasif`
- List categories:
  - `module_categories`
  - `modul_kategoriler`
- Run module:
  - `module_run <module_name> key=value ...`
  - `modul_calistir <modul_adi> anahtar=deger ...`
  - Example: `module_run kb_domain_whois domain=example.com`

Regional (country) management
- Show enabled countries:
  - `country_list` (alias: `ulke_liste`)
- Enable a country:
  - `country_enable <code>` (alias: `ulke_etkinlestir <kod>`)
- Disable a country:
  - `country_disable <code>` (alias: `ulke_devre_disi <kod>`)
- National mode (single country):
  - `country_set <code>` (alias: `ulke_ayarla <kod>`)
- Reload modules:
  - `reload_modules` (alias: `modulleri_yeniden_yukle`)

Language options
- Default language is set in `config/main_config.yaml` (`system.language`).
- Supported codes: `en`, `tr`, `ru`
- CLI currently displays bilingual English/Turkish messages; Russian help texts will be expanded incrementally.

## Project Layout

- `kb-osint/core/` — core system (loader, security, config, data manager)
- `kb-osint/interface/` — CLI and interactive shell
- `kb-osint/modules/` — modules
  - `core_modules/` — official module groups (domain, ip, email, social_media, advanced_search, person_research, corporate_osint)
  - `community_modules/` — community-contributed modules (analysis_reporting, visual_osint, integrations, etc.)
  - `user_modules/` — user-created modules
  - `regional/<country_code>/` — country-specific modules (e.g., `regional/tr/`)
- `kb-osint/reports/` — templates, generators, exporters
- `kb-osint/config/` — YAML configuration files
- `kb-osint/docs/` — documentation
  - English: `kb-osint/docs/user_guide/`
  - Turkish: `kb-osint/docs/kullanıcı_kılavuzu/`
- `kb-osint/tests/` — unit, integration, and performance tests
- `kb-osint/scripts/` — install and automation scripts
- `kb-osint/external/` — external assets and clients
- `kb-osint/backups/` — backups

## Tips

- Categories commonly used:
  - `domain`, `ip`, `email`, `social_media`, `advanced_search`, `person_research`, `corporate_osint`, `analysis`, `visual`, `reporting`, `tools`, `security`, `protocols`, `community_integrations`
- Regional modules are loaded only if the country code is enabled in the config (`regional.enabled_countries`) or set in national mode (`regional.country_code`).
- Keep API keys in `config/api_keys.yaml` or environment variables (see `.env.example`).

## Docker (optional)

Build and run the interactive CLI in a container:
```
docker build -t kb-osint .
docker run -it --rm kb-osint python kb-osint/kb.py
```
Use bind mounts if you want to persist reports or logs:
```
docker run -it --rm \
  -v "$PWD/kb-osint/reports:/app/kb-osint/reports" \
  -v "$PWD/kb-osint/logs:/app/kb-osint/logs" \
  kb-osint python kb-osint/kb.py
```

## Scenarios

- Exploring KB-OSINT
  - Set `regional.mode: international`
  - Leave `enabled_countries` empty
  - Run `module_list`, `module_categories`, and try `module_search <text>`
- Pilot (single country)
  - Set `regional.mode: national` and `country_code: "tr"` (example)
  - Or at runtime: `country_set tr` then `reload_modules`
  - Use `module_list detailed` to view required APIs and dependencies
- Full rollout
  - Enable multiple countries in `enabled_countries`
  - Add API keys to `config/api_keys.yaml`
  - Integrate reports output with your tooling (CSV/XML/SQL exporters)

## Roadmap / Upcoming

- SOCMINT (Social Media Intelligence) — coming in the next update
  - Username enumeration and cross-platform checks
  - Profile discovery, posts/media collection (respecting platform ToS)
  - Connection graphing, influence metrics, topic analysis
  - Alerts/monitoring for new activity

See the docs folder for detailed guides and examples.
