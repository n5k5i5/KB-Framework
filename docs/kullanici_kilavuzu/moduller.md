# Modüller Kılavuzu

KB-OSINT modül ekosistemi üç ana kaynaktan yükleme yapar:
- `moduller/cekirdek_moduller/` (resmi)
- `moduller/topluluk_modulleri/` (topluluk)
- `moduller/kullanici_modulleri/` (kullanıcı)

## Modül Manifesti
Zorunlu alanlar:
- `modul_adi`, `versiyon`, `yazar`, `aciklama`, `kategori`

Opsiyonel alanlar:
- `api_gereksinimleri`, `bagimliliklar`, `izinler`, `guvenlik_seviyesi`

## Kategoriler
- çekirdek: resmi destekli modüller
- topluluk: doğrulanmış geliştiricilerden modüller
- kullanıcı: kişisel/kurum içi modüller

## İzinler ve Güvenlik
- İzin setleri modülün kullanabileceği kaynakları tanımlar (örn: `http`, `dns`, `fs_read`)
- Güvenlik seviyesi: `yuksek`, `orta`, `dusuk`

## Modül Örnekleri (İskelet)
- `kb_domain.py`, `kb_ip.py`, `kb_email.py` (çekirdek)
- `kb_sosyal_medya.py`, `kb_advanced_scan.py` (topluluk)