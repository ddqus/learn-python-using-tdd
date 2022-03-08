import dataclasses
import json

import pytest


def test_dataclass_cannot_be_json():
    o = Test("n1")

    with pytest.raises(Exception) as exc_info:
        json.dumps(o)
    assert isinstance(exc_info.value, TypeError)
    assert "Object of type Test is not JSON serializable" == str(exc_info.value)


@dataclasses.dataclass
class Test:
    name: str
