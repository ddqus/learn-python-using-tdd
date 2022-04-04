def test_intersection():
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 5]

    intersection = list(set(list1).intersection(list2))

    assert intersection == [3, 5]
