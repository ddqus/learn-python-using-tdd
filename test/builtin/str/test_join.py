import pytest


def test_join():
    assert ",".join(["1", "2"]) == "1,2"


def test_join_iterable_accept_str_not_int():
    with pytest.raises(TypeError) as exc_info:
        ",".join(["1", 2])

    assert str(exc_info.value).startswith("sequence item")
