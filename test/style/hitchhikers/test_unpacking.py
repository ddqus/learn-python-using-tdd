def test_unpacking1():
    a, *rest = [1, 2, 3, 4]
    assert a == 1
    assert rest == [2, 3, 4]


def test_unpacking2():
    a, *middle, c = [1, 2, 3, 4, 5]
    assert a == 1
    assert middle == [2, 3, 4]
    assert c == 5


def test_rsplit():
    filename, ext = "test.file.png".rsplit(".", 1)
    assert filename == "test.file"
    assert ext == "png"


def test_ignore():
    filename, __, ext = "test.file.png".rpartition(".")
    assert filename == "test.file"
    assert __ == "."
    assert ext == "png"
