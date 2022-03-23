"""
https://docs.python.org/3/tutorial/inputoutput.html
https://docs.python.org/3/reference/lexical_analysis.html#f-strings
"""


def test_fstring_conversion():
    src_str = "a1`'-=!"
    assert f"{src_str}" == 'a1`\'-=!'
    assert f"{src_str!a}" == '"a1`\'-=!"'
    assert f"{src_str!s}" == 'a1`\'-=!'
    assert f"{src_str!r}" == '"a1`\'-=!"'


def test_fstring_multiline():
    dummy = "@"
    longstr = (
        f"a{dummy}"
        f"b{dummy}"
    )
    assert longstr == "a@b@"


def test_fstring_conversion():
    sut = "abc"
    assert str(sut) == "abc"
    assert str(f"{sut}") == "abc"
    assert str(f"{sut!r}") == "'abc'"
