def test():
    sut(1, 2, c=3)

    assert sut(1, 2) == 3
    assert sut(1, 2, custom_return="stop") == "stop"


def trace(func):
    def wrapper(*args, **kwargs):
        assert isinstance(args, tuple)
        assert isinstance(kwargs, dict)

        print(f"before - {func.__name__}({args}, {kwargs})")

        if "custom_return" in kwargs:
            return kwargs["custom_return"]

        result = func(*args, **kwargs)
        print(f"after result - {result}")
        return result

    return wrapper


@trace
def sut(a, b, c=None):
    return a + b
