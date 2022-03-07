import os

from dotenv import load_dotenv


def test_load():
    # given
    assert not os.getenv("DOTENV_DUMMY")

    # when
    load_dotenv()

    # then
    assert "dotenv_dummy" == os.getenv("DOTENV_DUMMY")
