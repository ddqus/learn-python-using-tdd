f1 = lambda x: x + 1
f2 = lambda x: x * 3


def test_compose():
    assert _compose(f1, f2)(2) == 9
    assert _compose(f2, f1)(2) == 7


def _compose(first, second):
    return lambda x: second(first(x))
