# Başlangıç

KB-OSINT'i başlatmak ve temel komutları çalıştırmak için bu kılavuzu izleyin.

## Kurulum

1. Bağımlılıkları yükleyin:
   ```
   pip install -r requirements.txt
   pip install -r kb-osint/requirements.txt
   ```

2. İsteğe bağlı API anahtarlarını `kb-osint/config/api_anahtarları.yaml` içine girin.

## Başlatma

- Interaktif kabuğu başlatmak için:
  ```
  python kb-osint/kb.py
  ```
  Açılan kabukta `yardim` komutuyla kullanılabilir komutları görebilirsiniz.

## Modül Listeleme

- Tüm modülleri listeleme:
  ```
  modul_liste
  ```
- Detaylı liste:
  ```
  modul_liste detayli
  ```
- Kategoriye göre:
  ```
  modul_liste kategori <kategori_adi>
  ```
- Arama:
  ```
  modul_ara <metin>
  ```

- Aktif/Pasif filtreleri:
  ```
  modul_liste aktif
  modul_liste pasif
  ```