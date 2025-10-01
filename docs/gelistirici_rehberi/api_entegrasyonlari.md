# API Entegrasyonları

Harici servislerle entegrasyon planı ve örnek iskeletler.

## API Yöneticisi (Örnek)
```python
class KB_API_Yoneticisi:
    def __init__(self, config):
        self.config = config
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'KB-OSINT/1.0.0',
            'Accept': 'application/json'
        })
```

### Shodan
- Endpoint: `https://api.shodan.io/shodan/host/{ip}`
- Anahtar: `KB_SHODAN_API`
- Rate limit ve hata politikaları

### VirusTotal
- Endpoint: `https://www.virustotal.com/api/v3/domains/{domain}`
- Header: `x-apikey`
- Çıktı normalizasyonu

### WHOIS
- Servis seçimi ve lisans uyumu
- Alternatif: yerel kütüphaneler (dnspython, python-whois)

## Bağdaştırıcı Mimarisi
- Her API için ayrı bağdaştırıcı sınıfı
- Ortak oturum ve hata işleme politikaları
- Cache ve throttling (ileri faz)