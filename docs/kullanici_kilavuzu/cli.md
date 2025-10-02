# CLI Tasarımı

Komut hiyerarşisi:

```
kb [ANA_KOMUT] [ALT_KOMUT] [PARAMETRELER] [SEÇENEKLER]

Ana Komutlar:
  hedef       Hedef yönetimi
  modul       Modül yönetimi
  tarama      OSINT tarama işlemleri
  rapor       Raporlama işlemleri
  sistem      Sistem yönetimi
  guvenlik    Güvenlik ayarları
```

Interaktif Kabuk (iskelet):
- Prompt: `KB-OSINT>`
- Komutlar dinamik olarak eklenebilir
- `yardim` ve `cikis` yerleşik komutlar

Renkli Çıktı:
- Başlık, başarı, hata ve bilgi mesajları ANSI kodlarıyla renklendirilir

## Modül Listeleme Komutları

- Tüm modülleri listeleme:
  ```
  modul_liste
  ```

- Detaylı modül bilgileri:
  ```
  modul_liste detayli
  ```

- Kategoriye göre listeleme:
  ```
  modul_liste kategori <kategori_adi>
  ```
  Örnek kategoriler: `domain`, `ip`, `email`, `sosyal_medya`, `kisi`, `kurumsal`, `gelismis_arama`, `analiz`, `gorsel`, `raporlama`, `turkiye`, `api`, `araclar`, `guvenlik`, `protokoller`, `topluluk_entegrasyon`

- Tüm kategorileri ve modül sayılarını gösterme:
  ```
  modul_kategoriler
  ```

- Modüllerde arama:
  ```
  modul_ara <metin>
  ```
  Örnek:
  ```
  modul_ara domain
  modul_ara shodan
  ```

- Sadece aktif/pasif modüller:
  ```
  modul_liste aktif
  modul_liste pasif
  ```

## Örnek Çıktılar

Temel Liste:
```
KB-OSINT MODÜL LİSTESİ
Toplam 8 modül yüklü
--------------------------------------------------------------------------------
 1. kb_domain_whois
     Açıklama: Domain WHOIS bilgilerini toplar.
     Versiyon: 0.1.0
     Kategori: domain
     Yazar: KB-OSINT Team
```

Kategori Listesi:
```
MODÜL KATEGORİLERİ
==============================
📁 domain: 5 modül
📁 ip: 5 modül
📁 email: 4 modül
📁 sosyal_medya: 4 modül
```

Arama Sonucu:
```
'domain' ARAMA SONUÇLARI (3 modül)
============================================================
 1. kb_domain_whois
     Açıklama: Domain WHOIS bilgilerini toplar.
     Versiyon: 0.1.0
     Kategori: domain
     Yazar: KB-OSINT Team
```

## Başlatma

- Uygulamayı başlatmak için:
  ```
  python main.py
  ```
  Ardından interaktif kabukta yukarıdaki komutları kullanabilirsiniz.