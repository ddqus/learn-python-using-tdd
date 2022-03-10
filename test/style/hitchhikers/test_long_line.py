from datetime import (
    datetime,
    date,
    time,
)


def test_split_long_line():
    # bad
    bad_insult = "insult insult insult " \
                 "insult insult insult " \
                 "insult insult"

    # good
    good_insult = (
        "insult insult insult "
        "insult insult insult "
        "insult insult"
    )

    assert bad_insult == good_insult


def test_import():
    assert datetime
    assert date
    assert time
