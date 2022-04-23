import pytest


@pytest.mark.parametrize("test_input, expected", [
    # sequnce: str, list, tuple
    ("2", ("2",)),
    ([3, 4], (3, 4)),
    ((5, 6), (5, 6)),

    # mapping: dict
    ({"a": 1, "b": 2}, ("a", "b")),

    # set: set
    ({7, 8}, (8, 7)),
])
def test_tuplable(test_input, expected):
    sut = tuple
    assert sut(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
    # numeric: int
    (1, "'int' object is not iterable"),

    # boolean: bool
    (True, "'bool' object is not iterable"),
    (False, "'bool' object is not iterable"),

    # etc: None
    (None, "'NoneType' object is not iterable"),
])
def test_cannot_tuplable(test_input, expected):
    sut = tuple

    with pytest.raises(TypeError) as excinfo:
        sut(test_input)
    assert str(excinfo.value) == expected
