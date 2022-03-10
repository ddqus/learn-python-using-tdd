def test_multiline_str():
    longstr1 = (
        "a"
        "b"
        "c"
    )
    assert "abc" == longstr1

    longstr2 = (
        "["
        "{}"
        "]"
    )
    assert isinstance(longstr2, str)
    assert "[a]" == longstr2.format("a")

    longstr3 = (
        "{{"
        "[{}]"
        "}}"
    )
    assert "{[b]}" == longstr3.format("b")
