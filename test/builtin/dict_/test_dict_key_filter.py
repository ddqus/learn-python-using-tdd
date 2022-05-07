origin = dict(a=1, b=2, c=3, d=4, e=5)
allowed = ["a", "b", "d"]
expected = dict(a=1, b=2, d=4)


def test():
    actual = {allow: origin[allow] for allow in allowed}
    assert actual == expected
