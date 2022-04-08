"""
https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects
"""


def test_dict_values():
    data = {
        "k1": (1, 2),
        "k2": (3,),
    }
    sut = data.values()

    assert not isinstance(sut, list)
    assert str(type(sut)) == "<class 'dict_values'>"
