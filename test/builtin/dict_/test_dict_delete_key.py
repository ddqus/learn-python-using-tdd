def test():
    sut = {'a': 1, 'b': 2, 'c': 3}

    del sut["a"]

    assert sut == {'b': 2, 'c': 3}
