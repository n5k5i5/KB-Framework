# Güvenlik Protokolleri

Bu doküman modül imzalama, izin sistemi ve sandbox politikalarını özetler.

## İmza Doğrulama
- Resmi modüller: `KB-OSINT_IMZA`
- Topluluk modülleri: geliştirici imzası
- Kullanıcı modülleri: opsiyonel imza

## Güvenlik Seviyeleri
- `yuksek`: sadece imzalı ve güvenilir modüller
- `orta`: imzalı + beyaz liste geliştiriciler
- `dusuk`: geliştirici modu; audit zorunlu

## İzinler ve Sandbox
- İzin setleri: `http`, `dns`, `fs_read`, `fs_write`, `subprocess`
- Sandbox/izole çalışma: kaynak ve erişim kotaları
- Audit log: ağ çağrıları ve dosya erişimlerinin izlenmesi