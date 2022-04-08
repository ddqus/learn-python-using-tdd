import io


def test_print_call_str():
    dummy_io = io.StringIO()
    sut = Sut()

    print(sut, file=dummy_io)
    assert dummy_io.getvalue() == '__str__ str\n'


def test_print_end():
    dummy_io = io.StringIO()
    sut = Sut()

    print(sut, file=dummy_io, end="@")
    assert dummy_io.getvalue() == '__str__ str@'


def test_print_list_call_repr():
    dummy_io = io.StringIO()
    sut = [Sut("a"), ]

    print(sut, file=dummy_io)
    assert dummy_io.getvalue() == "[__repr__ a]\n"


def test_print_tuple_call_repr():
    dummy_io = io.StringIO()
    sut = (Sut("a"),)

    print(sut, file=dummy_io)
    assert dummy_io.getvalue() == "(__repr__ a,)\n"


class Sut:
    name: str

    def __init__(self, name="str"):
        self.name = name

    def __str__(self):
        return f"__str__ {self.name}"

    def __repr__(self):
        return f"__repr__ {self.name}"
