def test_intersection():
    set1 = {1, 2, 3, 4, 5}
    set2 = {2, 4}

    intersection = set1.intersection(set2)

    assert intersection == {2, 4}
