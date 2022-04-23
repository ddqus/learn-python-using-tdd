import pytest

from app.tools import typetool


@pytest.mark.parametrize("test_input, expected", [
    # numeric: int
    (1, (1,)),

    # sequnce: str, list, tuple
    ("2", ("2",)),
    ("ab", ("ab",)),
    ([3, 4], (3, 4)),
    ((5, 6), (5, 6)),

    # mapping: dict
    ({"a": 1, "b": 2}, ("a", "b")),

    # set: set
    ({7, 8}, (8, 7)),

    # boolean: bool
    (True, (True,)),
    (False, (False,)),
])
def test(test_input, expected):
    sut = typetool.tuplify
    assert sut(test_input) == expected
    assert isinstance(sut(test_input), tuple)
