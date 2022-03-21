def test_function_is_callable():
    assert callable(callable_function)


def test_cannot_callable_class():
    sut = CannotCallableClass()
    assert not callable(sut)


def test_callable_class():
    sut = CallableClass()
    assert callable(sut)


def callable_function():
    pass


class CannotCallableClass:
    pass


class CallableClass:
    def __call__(self, *args, **kwargs):
        pass
