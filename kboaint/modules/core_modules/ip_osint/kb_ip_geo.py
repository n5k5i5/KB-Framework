# -*- coding: utf-8 -*-
"""IP GeoIP (ip-api.com)"""
from typing import Dict, Any

try:
    import requests
except Exception:
    requests = None

MANIFEST = {
    "modul_adi": "kb_ip_geo",
    "versiyon": "0.1.0",
    "yazar": "KB-OSINT Team",
    "aciklama": "IP için coğrafi konum bilgisi toplar.",
    "kategori": "ip",
    "api_gereksinimleri": [],
    "bagimliliklar": ["requests>=2.31.0"],
    "izinler": ["http"],
    "guvenlik_seviyesi": "orta",
    "aktif": True,
}

from kboaint.core.interface import KB_Modul_Arayuzu

class KB_IPGeo(KB_Modul_Arayuzu):
    metadata = MANIFEST

    def calistir(self, params: Dict[str, Any]) -> Dict[str, Any]:
        self.dogrula_parametreler(params)
        ip = (params.get("ip") or "").strip()
        if not ip:
            return {"durum": "hata", "mesaj": "Geçerli bir IP giriniz", "veri": {}}
        if not requests:
            return {"durum": "hata", "mesaj": "requests yüklü değil", "veri": {}}
        url = f"http://ip-api.com/json/{ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,query"
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            data = r.json()
            if data.get("status") != "success":
                return {"durum": "hata", "mesaj": data.get("message", "Sorgu başarısız"), "veri": {}}
            out = {
                "ip": data.get("query"),
                "continent": data.get("continent"),
                "country": data.get("country"),
                "region": data.get("regionName"),
                "city": data.get("city"),
                "lat": data.get("lat"),
                "lon": data.get("lon"),
                "isp": data.get("isp"),
                "org": data.get("org"),
                "as": data.get("as"),
            }
            return {"durum": "basarili", "mesaj": "GeoIP verisi alındı", "veri": out}
        except Exception as e:
            return {"durum": "hata", "mesaj": f"GeoIP isteği başarısız: {e}", "veri": {}}