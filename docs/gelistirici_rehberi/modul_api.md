# Modül Geliştirme API'si

Tüm modüller aşağıdaki arayüzü implement etmelidir:

```python
class KB_Modul_Arayuzu:
    def __init__(self):
        self.metadata = {
            "modul_adi": "",
            "versiyon": "1.0.0",
            "yazar": "",
            "aciklama": "",
            "kategori": "",
            "api_gereksinimleri": [],
            "bagimliliklar": [],
            "izinler": [],
            "guvenlik_seviyesi": "orta",
        }
    
    def initialize(self):
        pass

    def execute(self, hedef, parametreler=None):
        pass

    def validate(self):
        return True

    def cleanup(self):
        pass
```

## Modül Şablonu (Örnek)
```python
class KB_Domain_Modul(KB_Modul_Arayuzu):
    def __init__(self):
        super().__init__()
        self.metadata.update({
            "modul_adi": "kb_domain",
            "versiyon": "1.2.0",
            "yazar": "KB-OSINT Team",
            "aciklama": "Domain WHOIS ve DNS bilgileri toplama",
            "kategori": "domain",
            "api_gereksinimleri": ["whois_api", "dns_api"],
            "bagimliliklar": ["python-whois>=0.8.0", "dnspython>=2.1.0"],
            "izinler": ["ag_erisimi"],
            "guvenlik_seviyesi": "yuksek",
        })
    
    def execute(self, hedef, parametreler=None):
        return {"status": "success", "data": {"domain": hedef}}
```

## Yaşam Döngüsü
1. initialize
2. validate
3. execute
4. cleanup

## İzinler ve Güvenlik
- İmza doğrulama zorunluluğu güvenlik moduna bağlıdır
- `izinler` alanı: ağ erişimi, dosya yazma vb. yetkiler