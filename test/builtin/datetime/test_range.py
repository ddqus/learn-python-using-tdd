import datetime


def day_range(start_day, end_day):
    start = datetime.datetime.strptime(start_day, "%Y-%m-%d")
    end = datetime.datetime.strptime(end_day, "%Y-%m-%d")
    delta = end - start
    return [start + datetime.timedelta(days=i) for i in range(delta.days + 1)]


def test():
    start_day = "2021-12-30"
    end_day = "2022-01-02"
    expected = [
        "2021-12-30",
        "2021-12-31",
        "2022-01-01",
        "2022-01-02",
    ]

    sut = [d.strftime("%Y-%m-%d") for d in day_range(start_day, end_day)]
    assert sut == expected
