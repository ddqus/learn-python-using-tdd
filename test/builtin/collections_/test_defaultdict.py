import collections

import pytest


def test_int():
    sut = collections.defaultdict(int)
    assert sut["a"] == 0
    assert sut["b"] == 0

    with pytest.raises(TypeError) as exc_info:
        assert sut["c"]["d"] == 0
    assert exc_info.value.args[0] == "'int' object is not subscriptable"


def test_list():
    sut = collections.defaultdict(list)
    assert sut["a"] == []
    assert sut["b"] == []


def test_dict():
    sut = collections.defaultdict(dict)

    assert sut["a"] == {}

    with pytest.raises(KeyError) as exc_info:
        assert sut["b"]["c"] == []
    assert exc_info.value.args[0] == "c"


def test_None():
    sut = collections.defaultdict(None)

    with pytest.raises(KeyError) as exc_info:
        assert sut["a"] is None
    assert exc_info.value.args[0] == "a"
