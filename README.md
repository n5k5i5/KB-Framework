# KB-OSINT

Extensible OSINT platform with full directory layout and skeletal code.

## Start
```
python kb-osint/kb.py
```
Use the interactive shell to list modules and run commands.

## International / National (regional) modules
- Country-specific modules live under: `kb-osint/modüller/regional/<country_code>/`
- Configure via `kb-osint/config/ana_config.yaml`:
  ```yaml
  regional:
    mode: international        # international | national
    country_code: ""           # e.g., "tr"
    enabled_countries: []      # e.g., ["tr", "us"]
  ```
  - International mode: allow multiple country-specific modules via `enabled_countries`.
  - National mode: set `country_code` to load only that country's modules.

## Directory Summary
- çekirdek/: core system (loader, security, config)
- modüller/: official, community and user modules (category-based)
- arayüz/: CLI and interactive shell
- raporlar/: templates, generators and exporters
- veri/: database, cache and temporary data
- eklentiler/: plugin system
- utils/: helper tools
- docs/: user and developer documentation
  - English: `kb-osint/docs/user_guide/`
  - Turkish: `kb-osint/docs/kullanıcı_kılavuzu/`
- config/: YAML configuration files
- tests/: unit, integration and performance tests
- scripts/: installer and automation scripts
- external/: external dependencies/assets
- backups/: backup directories

## Roadmap / Upcoming
- SOCMINT (Social Media Intelligence) — coming in the next update
  - Username enumeration and cross-platform checks
  - Profile discovery, posts/media collection (respecting platform ToS)
  - Connection graphing, influence metrics, topic analysis
  - Alerts/monitoring for new activity

See the docs folder for details.
