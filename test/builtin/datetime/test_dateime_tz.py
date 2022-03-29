import datetime


def test_without_tz():
    dt = datetime.datetime(2020, 1, 2, 3, 4, 5, 6)
    assert not dt.tzinfo
    assert str(dt) == "2020-01-02 03:04:05.000006"


def test_with_tz():
    dt = datetime.datetime(2020, 1, 2, 3, 4, 5, 6, tzinfo=datetime.timezone.utc)
    assert dt.tzinfo
    assert dt.tzinfo == datetime.timezone.utc


def test_tz_str():
    dt = datetime.datetime(2020, 1, 2, 3, 4, 5, 6, tzinfo=datetime.timezone.utc)
    assert str(dt) == "2020-01-02 03:04:05.000006+00:00"
