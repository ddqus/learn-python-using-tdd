def test_complicated_condition():
    # bad
    if (1 + 3 + 5 + 7 + 9 == 1) and (2 + 4 + 6 + 8 == 1):
        assert False

    # good
    def cond1():
        return 1 + 3 + 5 + 7 + 9 == 1

    def cond2():
        return 2 + 4 + 6 + 8 == 1

    if cond1() and cond2():
        assert False
