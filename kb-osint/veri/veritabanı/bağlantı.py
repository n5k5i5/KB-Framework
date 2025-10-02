"""
Veritabanı bağlantı yöneticisi (iskelet).
"""
class Baglanti:
    def __init__(self, dsn: str = ""):
        self.dsn = dsn