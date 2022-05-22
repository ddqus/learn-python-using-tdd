def test():
    request("a", "b", c=1)
    assert request(1, 0) == 1
    assert request(2, 0) == 1


def cache(func):
    repo = {}

    def wrapper(*args, **kwargs):
        key = str(args[1:]) + str(kwargs)
        if key in repo:
            return repo[key]

        result = func(*args, **kwargs)

        repo[key] = result

        return result

    return wrapper


@cache
def request(arg, arg2, c=None):
    return arg
