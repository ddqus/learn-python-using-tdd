def test_dict_pop_first():
    data = {
        "k1": (1, 2),
        "k2": (3,),
    }
    sut = list(data.values())[0]
    assert sut == (1, 2)
