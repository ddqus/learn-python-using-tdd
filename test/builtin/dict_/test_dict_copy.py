import copy


def test_equal_operator_refer_same_object():
    params = {
        "age": "10",
        "sql": "select",
    }
    sut = params

    assert params == {
        "age": "10",
        "sql": "select",
    }
    assert sut == {
        "age": "10",
        "sql": "select",
    }

    del sut["sql"]

    assert params != {
        "age": "10",
        "sql": "select",
    }
    assert params == {
        "age": "10",
    }
    assert sut == {
        "age": "10",
    }


def test_copy_return_different_object():
    params = {
        "age": "10",
        "sql": "select",
    }
    sut = params.copy()

    assert params == {
        "age": "10",
        "sql": "select",
    }
    assert sut == {
        "age": "10",
        "sql": "select",
    }

    del sut["sql"]

    assert params == {
        "age": "10",
        "sql": "select",
    }
    assert sut == {
        "age": "10",
    }


def test_copy_refer_same_object_if_dict_contain_collection():
    params = {
        "age": [10, 20],
        "sql": "select",
    }
    sut = params.copy()

    assert params == {
        "age": [10, 20],
        "sql": "select",
    }
    assert sut == {
        "age": [10, 20],
        "sql": "select",
    }

    sut["age"].append(30)

    assert params != {
        "age": [10, 20],
        "sql": "select",
    }
    assert params == {
        "age": [10, 20, 30],
        "sql": "select",
    }
    assert sut == {
        "age": [10, 20, 30],
        "sql": "select",
    }


def test_deepcopy_return_completely_different_object():
    params = {
        "age": [10, 20],
        "sql": "select",
    }
    sut = copy.deepcopy(params)

    assert params == {
        "age": [10, 20],
        "sql": "select",
    }
    assert sut == {
        "age": [10, 20],
        "sql": "select",
    }

    sut["age"].append(30)

    assert params == {
        "age": [10, 20],
        "sql": "select",
    }
    assert sut == {
        "age": [10, 20, 30],
        "sql": "select",
    }
