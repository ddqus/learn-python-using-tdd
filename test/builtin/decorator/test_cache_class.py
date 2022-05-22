class MemCache:
    def __init__(self, func):
        self.func = func
        self.repo = {}

    def __call__(self, *args, **kwargs):
        key = str(args[1:]) + str(kwargs)
        
        if key in self.repo:
            return self.repo[key]

        result = self.func(*args, **kwargs)

        self.repo[key] = result

        return result


def test():
    request("a", "b", c=1)
    assert request(1, 0) == 1
    assert request(2, 0) == 1


@MemCache
def request(arg, arg2, c=None):
    return arg
