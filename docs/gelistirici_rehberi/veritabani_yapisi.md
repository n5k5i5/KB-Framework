# Veritabanı Yapısı

Üretim hedefi: sonuçların ve artefaktların kalıcı olarak saklanması.

## SQLAlchemy Modelleri (Örnek)
```python
from sqlalchemy import create_engine, Column, String, Integer, DateTime, Text, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class KB_Hedef(Base):
    __tablename__ = 'kb_hedefler'
    id = Column(Integer, primary_key=True)
    hedef = Column(String(255), nullable=False)
    tip = Column(String(50))  # domain, ip, email
    eklenme_tarihi = Column(DateTime)
    guncellenme_tarihi = Column(DateTime)
    etiketler = Column(JSON)  # ["musteri", "acil", "test"]

class KB_Tarama_Sonucu(Base):
    __tablename__ = 'kb_tarama_sonuclari'
    id = Column(Integer, primary_key=True)
    hedef_id = Column(Integer)
    modul_adi = Column(String(100))
    tarama_tarihi = Column(DateTime)
    sonuc = Column(JSON)
    basarili = Column(Boolean)
    hata_mesaji = Column(Text)

class KB_Modul(Base):
    __tablename__ = 'kb_moduller'
    id = Column(Integer, primary_key=True)
    modul_adi = Column(String(100), unique=True)
    versiyon = Column(String(20))
    yazar = Column(String(100))
    aciklama = Column(Text)
    kategori = Column(String(50))
    aktif = Column(Boolean, default=True)
    kayit_tarihi = Column(DateTime)
```

## Saklama Politikaları
- PII/PHI verileri için maskeleme
- Silme ve arşiv periyotları
- Erişim kontrolü ve audit

## Performans ve İndeksleme
- hedef/modül tablosunda indeksler
- büyük JSON alanları için ayrıştırılmış saklama (ileri faz)