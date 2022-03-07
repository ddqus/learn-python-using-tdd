import os


def test_load():
    assert "dotenv_dummy" == os.getenv("DOTENV_DUMMY")
