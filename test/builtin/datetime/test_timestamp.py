import datetime
import time


def test_current_timestamp():
    sut = time.time()
    assert sut > 1600000000


def test_datetime_to_unix_timestamp():
    sut = time.mktime(datetime.datetime(2021, 2, 3, 4, 5, 6).timetuple())

    assert sut == 1612292706


def test_str_to_datetime():
    str_date = "2021-02-03 04:05:06"

    sut = datetime.datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")
    assert sut.year == 2021
    assert sut.month == 2
    assert sut.day == 3
    assert sut.hour == 4
    assert sut.minute == 5
    assert sut.second == 6


def test_formatting_timestamp():
    str_date = "2021-02-03 04:05:06"
    date_time = datetime.datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")

    sut = time.mktime(date_time.timetuple())

    assert sut == 1612292706


def test_formatting_from_timestamp():
    timestamp = 1612292706
    date_time = datetime.datetime.fromtimestamp(timestamp)

    sut = date_time.strftime("%Y-%m-%d %H:%M:%S")

    assert sut == "2021-02-03 04:05:06"


def test_millisecond_timestamp():
    def _timestamp_to_second_if_millisecond(timestamp):
        if len(str(timestamp)) == 13:
            return timestamp // 1000
        return timestamp

    assert _timestamp_to_second_if_millisecond(1612292706123) == 1612292706
    assert _timestamp_to_second_if_millisecond(1612292706) == 1612292706
