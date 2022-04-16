def test_merge():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}

    sut = dict1 | dict2

    assert sut == {'a': 1, 'b': 3, 'c': 4}


def test_merge_reverse():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}

    sut = dict2 | dict1

    assert sut == {'a': 1, 'b': 2, 'c': 4}


def test_merge_using_kwargs():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}

    sut = {**dict1, **dict2}

    assert sut == {'a': 1, 'b': 3, 'c': 4}
