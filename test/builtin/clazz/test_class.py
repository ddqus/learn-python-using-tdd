def test_class_name_to_str():
    t = Test()
    assert "Test" == t.__class__.__name__
    assert "Test" == t.class_name()


class Test:
    def class_name(self):
        return self.__class__.__name__
