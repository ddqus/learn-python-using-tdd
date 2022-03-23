import json

import pytest


def test_json():
    assert json.dumps({"k": "v"}) == '{"k": "v"}'


def test_class_raise_serializable():
    with pytest.raises(TypeError) as exc_info:
        json.dumps(Test())

    assert str(exc_info.value) == "Object of type Test is not JSON serializable"


class Test:
    pass
