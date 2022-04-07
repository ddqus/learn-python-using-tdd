def test_include_single():
    fixture = "abcdefg"

    assert "bc" in fixture
    assert "bd" not in fixture


def test_include_multi():
    fixture = "abcdefg"
    matches = ["bc", "bd"]

    assert any(x in fixture for x in matches)
    assert not all(x in fixture for x in matches)
