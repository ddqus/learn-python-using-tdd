import pytest


def test_extend_need_iterator():
    sut = []

    with pytest.raises(TypeError) as exc_info:
        sut.extend(1)

    assert str(exc_info.value) == "'int' object is not iterable"


def test_extend_one():
    sut = []
    assert sut == []

    sut.extend([1])

    assert sut == [1]


def test_extend_1st_dimension():
    sut = []
    assert sut == []

    sut.extend([1, 2, 3])

    assert sut == [1, 2, 3]


def test_extend_not_flatten():
    sut = []
    assert sut == []

    sut.extend([[1, 2], [3, 4]])

    assert sut == [[1, 2], [3, 4]]
