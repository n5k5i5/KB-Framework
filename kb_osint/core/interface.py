class KB_Modul_Arayuzu:
    """
    Tüm modüllerin implement etmesi gereken arayüz.
    Not: Python Unicode kimlikleri desteklese de pratikte ASCII isimlendirme tercih edilmiştir.
    """

    def __init__(self):
        self.metadata = {
            "modul_adi": "",
            "versiyon": "1.0.0",
            "yazar": "",
            "aciklama": "",
            "kategori": "",  # domain, ip, email, sosyal_medya
            "api_gereksinimleri": [],  # shodan, virustotal, hunter
            "bagimliliklar": [],       # python kütüphaneleri
            "izinler": [],             # ag_erisimi, dosya_yazma
            "guvenlik_seviyesi": "orta",  # dusuk, orta, yuksek
        }

    def initialize(self):
        """Modül başlangıç konfigürasyonu"""
        pass

    def execute(self, hedef, parametreler=None):
        """Ana çalıştırma metodu"""
        if parametreler is None:
            parametreler = {}
        raise NotImplementedError("execute() modül tarafından implement edilmeli")

    def validate(self):
        """Gereksinim kontrolü"""
        return True

    def cleanup(self):
        """Kaynak temizleme"""
        pass