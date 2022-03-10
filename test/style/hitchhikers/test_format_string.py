def test_join_bad():
    s = ""
    for c in (97, 98, 99):
        s += chr(c)
    assert s == "abc"


def test_join_good():
    s = []
    for c in (97, 98, 99):
        s.append(chr(c))
    assert "".join(s) == "abc"


def test_join_best():
    r = (97, 98, 99)
    s = [chr(c) for c in r]
    assert "".join(s) == "abc"


def test_format_bad():
    adj = "red"
    noun = "hamlet"

    s = "%s %s" % (adj, noun)
    assert s == "red hamlet"


def test_format_good():
    adj = "red"
    noun = "hamlet"

    s = "{} {}".format(adj, noun)
    assert s == "red hamlet"


def test_format_best():
    adj = "red"
    noun = "hamlet"

    s = "{noun} {adj}".format(adj=adj, noun=noun)
    assert s == "hamlet red"
