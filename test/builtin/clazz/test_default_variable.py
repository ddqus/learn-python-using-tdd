def test_str_is_not_affected():
    b1 = Base()
    b2 = Base()

    assert "n" == b1.name
    assert "n" == b2.name

    b1.name = "n1"
    assert "n1" == b1.name
    assert "n" == b2.name


def test_str_is_not_affected_with_init():
    sut1 = BaseWithInit()
    sut2 = BaseWithInit()

    assert sut1.name == "n"
    assert sut2.name == "n"

    sut1.name = "n1"

    assert sut1.name == "n1"
    assert sut2.name == "n"


def test_list_is_affected():
    b1 = Base()
    b2 = Base()

    assert not b1.assets
    assert not b2.assets

    b1.assets.append("a")

    assert ["a"] == b1.assets
    # b2는 변경하지 않았는데 영향 받음
    assert ["a"] == b2.assets


def test_list_is_not_affected_with_init():
    sut1 = BaseWithInit()
    sut2 = BaseWithInit()

    assert not sut1.assets
    assert not sut2.assets

    sut1.assets.append("a")

    assert sut1.assets == ["a"]
    assert not sut2.assets


def test_int():
    b1 = Base()
    b2 = Base()

    assert b1.num == 10
    assert b2.num == 10

    b1.num += 1
    assert b1.num == 11
    assert b2.num == 10


def test_int_with_init():
    sut1 = BaseWithInit()
    sut2 = BaseWithInit()

    assert sut1.num == 10
    assert sut2.num == 10

    sut1.num += 1

    assert sut1.num == 11
    assert sut2.num == 10


class Base:
    name: str = "n"
    num: int = 10
    assets = []


class BaseWithInit:
    name: str
    num: int
    assets: list

    def __init__(self):
        self.name = "n"
        self.num = 10
        self.assets = []
