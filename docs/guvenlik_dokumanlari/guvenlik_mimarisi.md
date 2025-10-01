# Güvenlik Mimarisi

İmza doğrulama, izin politikaları ve sandbox ilkeleri.

## Modül İmzalama Sistemi
- Hash tabanlı imza (SHA-256)
- Resmi modüller için kayıtlı imzalar
- Topluluk geliştirici listesi ve imza doğrulama

## Güvenlik Politikaları
- `config/guvenlik_politikalari.yaml` dosyasında tanımlıdır
- `yuksek`, `orta`, `dusuk` modları ve izin setleri

## Statik ve Çalışma Zamanı Denetimleri
- Tehlikeli fonksiyonların statik tespiti
- Çalışma zamanında izin enforcement (ileri faz)