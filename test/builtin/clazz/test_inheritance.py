logs = []


def test_inheritance_order():
    assert not logs
    Child()
    assert 4 == len(logs)
    assert "init:parent" == logs[0]
    assert "<bound method Parent._override" == logs[1][0:30]
    assert "override:parent" == logs[2]
    assert "init:child" == logs[3]


def test_inheritance_override_order():
    global logs
    logs = []
    assert not logs

    OverrideChild()

    assert 3 == len(logs)
    assert "init:parent" == logs[0]
    assert "<bound method OverrideChild._o" == logs[1][0:30]
    assert "override:child" == logs[2]


class Parent:
    def __init__(self):
        logs.append("init:parent")
        logs.append(str(self._override))
        self._override()

    def _override(self):
        logs.append("override:parent")


class Child(Parent):
    def __init__(self):
        super().__init__()
        logs.append("init:child")


class OverrideChild(Parent):
    def _override(self):
        logs.append("override:child")
