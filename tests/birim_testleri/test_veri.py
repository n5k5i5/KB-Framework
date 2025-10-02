def test_veri_import():
    import importlib
    assert importlib.import_module("veri") is not None