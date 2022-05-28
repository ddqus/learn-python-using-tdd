def test():
    key = "k"
    sut = {}

    assert not sut.get(key)

    sut[key] = {"v": "1"}
    assert sut.get(key) == {"v": "1"}

    sut[key].update({"v": "2"})
    assert sut.get(key) == {"v": "2"}


def _create_row(i):
    return dict(
        key=f"k{i}",
        value=f"v{i}",
    )


def test_pass_by_value_problem():
    sut = DictDb()

    key = "key"
    value1 = _create_row(1)
    value2 = _create_row(2)
    assert value1 == {"key": "k1", "value": "v1"}
    assert value2 == {"key": "k2", "value": "v2"}

    sut.set(key, value1)
    sut.set(key, value2)

    assert value1 != {"key": "k1", "value": "v1"}
    assert value1 == {"key": "k2", "value": "v2"}
    assert value2 == {"key": "k2", "value": "v2"}


def test_pass_by_value_problem_solution1():
    sut = DictDb2()

    key = "key"
    value1 = _create_row(1)
    value2 = _create_row(2)
    assert value1 == {"key": "k1", "value": "v1"}
    assert value2 == {"key": "k2", "value": "v2"}

    sut.set(key, value1)
    sut.set(key, value2)

    assert value1 == {"key": "k1", "value": "v1"}
    assert value1 != {"key": "k2", "value": "v2"}
    assert value2 == {"key": "k2", "value": "v2"}


class DictDb:
    def __init__(self):
        self.db = {}

    def set(self, key, value):
        if key in self.db:
            self.db[key].update(value)
        else:
            self.db[key] = value


class DictDb2:
    def __init__(self):
        self.db = {}

    def set(self, key, value):
        if key in self.db:
            self.db[key].update(value)
        else:
            self.db[key] = dict(value)
