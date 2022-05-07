import os


def test_get_all_keys():
    keys = list(os.environ.keys())
    assert "OS" in keys
    assert "PATH" in keys
