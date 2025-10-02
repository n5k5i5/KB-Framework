# Troubleshooting

Common issues and solutions.

- No modules loaded:
  - Ensure you installed requirements.
  - Verify you started the shell from the project root: `python kb-osint/kb.py`.

- Country-specific modules missing:
  - Add the country code to `regional.enabled_countries` in `kb-osint/config/ana_config.yaml` (e.g., `["tr"]`).

- API errors:
  - Check `kb-osint/config/api_anahtarları.yaml` for missing or invalid keys.
  - Ensure outbound network is allowed for your environment.