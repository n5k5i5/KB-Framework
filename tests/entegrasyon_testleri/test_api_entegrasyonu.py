def test_config_api_keys_contains_key():
    with open("config/api_anahtarları.yaml", "r", encoding="utf-8") as f:
        content = f.read()
    assert "api_anahtarlari" in content