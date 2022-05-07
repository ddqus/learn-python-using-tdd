fields = ["date", "total"]
rows = [
    [1, 2],
    [3, 4],
]
expected = [
    {
        "date": 1,
        "total": 2,
    },
    {
        "date": 3,
        "total": 4,
    },
]


def test_zip_with_comprehension():
    sut = []
    for row in rows:
        sut.append({x: y for x, y in zip(fields, row)})

    assert sut == expected


def test_using_pylint_guide():
    sut = []
    for row in rows:
        sut.append(dict(zip(fields, row)))

    assert sut == expected


def test_to_single_line():
    sut = [dict(zip(fields, row)) for row in rows]

    assert sut == expected
