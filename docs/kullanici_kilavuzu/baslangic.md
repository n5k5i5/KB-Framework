# KB-OSINT Başlangıç Kılavuzu

Bu doküman KB-OSINT sisteminin kurulumu, yapılandırması ve ilk kullanımına dair özet içerir.

## Kurulum (MVP)
- Python 3.10+
- `requirements.txt` içeriğine göre bağımlılık kurulumu (ileride ayrıntılandırılacak)
- Ortam değişkenlerini `.env` veya sistem ortamına ekleyin

## Yapılandırma
- `config/kb_config.yaml` merkezi yapılandırma dosyası:
  - sistem, moduller, api, raporlama, guvenlik bölümleri
- Ortam değişkenleri:
  - `KB_SHODAN_API`, `KB_VIRUSTOTAL_API`, `KB_HUNTER_API`

## Dosya Yapısı (Özet)
- `moduller/` → çekirdek, topluluk ve kullanıcı modülleri
- `raporlar/` → çıktıların kaydedildiği klasör
- `docs/` → kullanıcı ve geliştirici dokümanları

## İlk Adımlar
1. `config/kb_config.yaml` dosyasını ihtiyaçlarınıza göre özelleştirin
2. Ortam değişkenlerini `.env.example` dosyasına göre ayarlayın
3. Modül keşfi ve raporlama ileride CLI üzerinden sağlanacaktır (iskele aşaması)