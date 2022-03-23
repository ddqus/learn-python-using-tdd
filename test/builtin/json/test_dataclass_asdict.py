import dataclasses
import json

import pytest


def test_dataclass_asdict():
    child = Child("c")
    assert json.dumps(dataclasses.asdict(child)) == '{"name": "c"}'


def test_nested():
    parent = Parent("p1", (
        Child("c1"),
        Child("c2"),
    ))
    assert json.dumps(dataclasses.asdict(parent)) \
           == '{"name": "p1", "childs": [{"name": "c1"}, {"name": "c2"}]}'


def test_nested_with_not_dataclass_raise_error():
    parent = Parent("p1", (
        NotDataclass("n1"),
    ))
    with pytest.raises(Exception) as exc_info:
        json.dumps(dataclasses.asdict(parent))

    assert isinstance(exc_info.value, TypeError)
    assert "not JSON serializable" in str(exc_info.value)


@dataclasses.dataclass
class Child:
    name: str


class NotDataclass:
    name: str

    def __init__(self, name):
        self.name = name


@dataclasses.dataclass
class Parent:
    name: str
    childs: tuple
