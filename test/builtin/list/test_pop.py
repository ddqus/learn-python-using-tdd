def test_pop_remove_last():
    sut = [1, 2, 3]
    assert sut.pop() == 3
    assert sut == [1, 2]


def test_pop_support_index():
    sut = [1, 2, 3]
    assert sut.pop(0) == 1
    assert sut == [2, 3]
