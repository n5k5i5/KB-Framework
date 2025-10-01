# Modül Geliştirme Rehberi

Bu doküman modül manifesti, kategori ve izin yapısı ile yaşam döngüsü olaylarını tanımlar.

## Manifest
Zorunlu alanlar:
- `modul_adi`, `versiyon`, `yazar`, `aciklama`, `kategori`

Opsiyonel alanlar:
- `api_gereksinimleri`, `bagimliliklar`, `izinler`, `guvenlik_seviyesi`

Ek öneriler:
- `uyumluluk` (core API aralığı), `kaynak_kotalari`, `yetenekler`
- Giriş/çıkış şemaları

## Yaşam Döngüsü
1. Keşif
2. Doğrulama
3. Yükleme
4. Kayıt
5. Yapılandırma
6. Çalıştırma
7. Temizleme

## Test ve Doğrulama
- Smoke test ve manifest doğrulama
- Bağımlılık güvenliği (CVE tarama)