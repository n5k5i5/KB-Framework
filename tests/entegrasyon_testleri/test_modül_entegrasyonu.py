def test_modul_manifest_exists():
    # Basit kontrol: örnek modül dosyalarından MANIFEST beklenir
    import importlib.util
    import os
    path = os.path.join("modüller", "çekirdek_modüller", "domain_osint", "kb_domain_whois.py")
    spec = importlib.util.spec_from_file_location("kb_domain_whois", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert hasattr(mod, "MANIFEST")