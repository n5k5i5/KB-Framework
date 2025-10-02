# Başlangıç

KB-OSINT'i başlatmak ve temel komutları çalıştırmak için bu kılavuzu izleyin.

## Kurulum

1. Bağımlılıkları yükleyin:
   ```
   pip install -r requirements.txt
   pip install -r kb-osint/requirements.txt
   ```

2. İsteğe bağlı API anahtarlarını `kb-osint/config/api_anahtarları.yaml` içine girin.

3. Uluslararası kullanım (opsiyonel):
   - `kb-osint/config/ana_config.yaml` içinde dil ve bölgesel modülleri ayarlayın:
     ```yaml
     sistem:
       dil: "en"  # veya "tr"
     regional:
       enabled_countries: []  # örn: ["tr", "us"]
     ```
   - Varsayılan olarak ülkeye özel modüller yüklenmez. TR modüllerini yüklemek için `enabled_countries` listesine `tr` ekleyin.

## Başlatma

- Interaktif kabuğu başlatmak için:
  ```
  python kb-osint/kb.py
  ```
  Açılan kabukta `yardim` veya `help` komutuyla kullanılabilir komutları görebilirsiniz.

## Modül Listeleme

- Tüm modülleri listeleme:
  ```
  modul_liste
  module_list
  ```
- Detaylı liste:
  ```
  modul_liste detayli
  module_list detailed
  ```
- Kategoriye göre:
  ```
  modul_liste kategori <kategori_adi>
  module_list category <category>
  ```
- Arama:
  ```
  modul_ara <metin>
  module_search <text>
  ```

- Aktif/Pasif filtreleri:
  ```
  modul_liste aktif
  modul_liste pasif
  module_list active
  module_list inactive
  ```