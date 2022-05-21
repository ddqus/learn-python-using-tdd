import os

import pytest


def test_windows_has_no_uname():
    with pytest.raises(AttributeError) as exc_info:
        os.uname()

    assert str(exc_info.value) == "module 'os' has no attribute 'uname'"
