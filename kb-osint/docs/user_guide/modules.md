# Modules

KB-OSINT modules are grouped into categories. Use the commands below to browse them.

## Commands

- List all:
  ```
  module_list
  ```

- Detailed:
  ```
  module_list detailed
  ```

- By category:
  ```
  module_list category <category>
  ```
  Example categories: `domain`, `ip`, `email`, `social_media`, `person`, `company`, `advanced_search`, `analysis`, `visual`, `reporting`, `api`, `tools`, `security`, `protocols`, `community_integration`

- Show categories:
  ```
  module_categories
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

## Example Output

```
KB-OSINT MODULE LIST
Total 50+ modules loaded
--------------------------------------------------------------------------------
 1. kb_domain_whois
     Description: Collects domain WHOIS information.
     Version: 0.1.0
     Category: domain
     Author: KB-OSINT Team
```