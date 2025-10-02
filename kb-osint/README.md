# KB-OSINT

Tam modüler ve genişletilebilir OSINT sistemi için iskelet dizin yapısı ve dosyalar.

## Başlatma

- CLI:
  ```
  python kb_cli.py
  ```

- API:
  ```
  python kb_api.py
  ```

## Dizin Özeti

- çekirdek/: çekirdek sistem bileşenleri
- modüller/: çekirdek, topluluk ve kullanıcı modülleri
- arayüz/: CLI ve interaktif kabuk
- raporlar/: şablonlar, oluşturucular ve dışa aktarım
- veri/: veritabanı, önbellek ve geçici veri
- eklentiler/: resmi, topluluk ve kullanıcı eklentileri
- utils/: yardımcı araçlar
- docs/: kullanıcı ve geliştirici dokümantasyonu
- config/: yapılandırma dosyaları
- tests/: test dosyaları
- scripts/: otomasyon scriptleri
- external/: harici kaynaklar
- backups/: yedekler

Bu iskelet ilerleyen sürümlerde işlevsel kodlarla genişletilecektir.