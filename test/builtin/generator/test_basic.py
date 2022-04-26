from collections import deque


def test_map_return_generator_not_result():
    target = []

    result = map(target.append, [1, 2, 3])

    assert isinstance(result, map)

    assert target != [1, 2, 3]
    assert target == []


def test_list_run_generator():
    target = []

    result = list(map(target.append, [1, 2, 3]))

    assert isinstance(result, list)

    assert target == [1, 2, 3]


def test_all_is_stop_generator_after_false():
    target = []

    result = all(map(target.append, [1, 2, 3]))

    assert result == False

    assert target == [1]


def test_any_is_run_all_generator():
    target = []

    result = any(map(target.append, [1, 2, 3]))

    assert result == False

    assert target == [1, 2, 3]


def test_deque_run_generator():
    target = []

    result = deque(map(target.append, [1, 2, 3]))

    assert isinstance(result, deque)

    assert target == [1, 2, 3]
