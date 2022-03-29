def test_append_one():
    sut = []
    assert not sut

    sut.append(1)
    assert sut == [1]

    sut.append(2)
    assert sut == [1, 2]


def test_append_list():
    sut = []
    assert not sut

    sut.append([1, 2])
    assert sut == [[1, 2]]
    assert sut != [1, 2]
