# Getting Started

Follow this guide to install and start KB-OSINT.

## Installation

1. Install dependencies:
   ```
   pip install -r requirements.txt
   pip install -r kb-osint/requirements.txt
   ```

2. Optional API keys:
   - Put your keys in `kb-osint/config/api_anahtarları.yaml`.

3. International / National setup (optional):
   - Configure language and regional modules in `kb-osint/config/ana_config.yaml`:
     ```yaml
     sistem:
       dil: "en"  # or "tr"
     regional:
       mode: international        # international | national
       country_code: ""           # e.g., "tr"
       enabled_countries: []      # e.g., ["tr", "us"]
     ```
   - International mode: use `enabled_countries` to allow multiple country-specific modules.
   - National mode: set `country_code` (e.g., `tr`) to load only that country's modules.

## Run the interactive shell

```
python kb-osint/kb.py
```

Use `help` to list available commands.

## Module listing commands

- List all modules:
  ```
  module_list
  ```
- Detailed list:
  ```
  module_list detailed
  ```
- Filter by category:
  ```
  module_list category <category>
  ```
- Search:
  ```
  module_search <text>
  ```
- Active/Inactive:
  ```
  module_list active
  module_list inactive
  ```