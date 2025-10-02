def test_cekirdek_import():
    import importlib
    assert importlib.import_module("çekirdek") is not None