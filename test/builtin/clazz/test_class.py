import importlib

from app.clazz import Dummy


def test_class_name_to_str():
    t = Test()
    assert "Test" == t.__class__.__name__
    assert "Test" == t.class_name()


class Test:
    def class_name(self):
        return self.__class__.__name__


def test_class_name_with_module():
    dummy = Dummy()

    assert "Dummy" == dummy.__class__.__name__
    assert "app.clazz.dummy" == dummy.__module__

    assert "app.clazz.dummy.Dummy" == \
           ".".join(map(str, [dummy.__module__, dummy.__class__.__qualname__]))


def test_create_class_from_fqn():
    module_name = "app.clazz.dummy"
    class_name = "Dummy"

    module = importlib.import_module(module_name)
    class_ = getattr(module, class_name)
    o = class_()
    assert isinstance(o, Dummy)
    assert "dum" == o.dummy()
