from app.tools import typetool

DATA = {
    "k1": [1, 2, 3],
    "k2": "s2",
    "k3": (4, 5),
}


def sut(dictobj: dict, sep=","):
    tuplized = {key: typetool.tuplify(value) for key, value in dictobj.items()}

    stringified = {key: tuple(map(str, value)) for key, value in tuplized.items()}

    joined = {key: sep.join(value) for key, value in stringified.items()}

    return joined


def test():
    result = sut(DATA, sep=".")
    expected = {
        "k1": "1.2.3",
        "k2": "s2",
        "k3": "4.5",
    }
    assert result == expected


def test_query_params():
    result = sut(DATA, sep=",")
    query_params = "&".join([f"{key}={value}" for key, value in result.items()])
    assert query_params == "k1=1,2,3&k2=s2&k3=4,5"
