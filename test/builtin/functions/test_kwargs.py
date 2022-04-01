def test_setup():
    assert sut(cpu="Intel", memory="4GB") == {"cpu": "Intel", "memory": "4GB"}


args = {
    "cpu": "Intel",
    "memory": "4GB",
}


def test_dict_is_treated_as_first_argument():
    assert sut(args) != {"cpu": "Intel", "memory": "4GB"}
    assert sut(args) == {'cpu': {'cpu': 'Intel', 'memory': '4GB'}, 'memory': None}


def test_unpacking_dict():
    """
    https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
    """
    assert sut(**args) == {"cpu": "Intel", "memory": "4GB"}


def sut(cpu=None, memory=None):
    return {
        "cpu": cpu,
        "memory": memory,
    }
