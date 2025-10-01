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