import unittest

from parameterized import parameterized


class MyTestCase(unittest.TestCase):
    """
    https://docs.python.org/3.10/library/stdtypes.html#str.endswith
    """

    @parameterized.expand([
        ["a/b/c", "c", True],
        ["a/b/c", "/c", True],
        ["a/b/c", "b/c", True],
        ["a/b/c", "/b/c", True],
        ["a/b/c", "a/b/c", True],
        ["a/b/c", "c/", False],
        ["a/b/c", "/c/", False],
        ["a/b/c", "b/c/", False],
        ["a/b/c", "/b/c/", False],
        ["a/b/c", "a/b/c/", False],
    ])
    def test_endswith(self, string, endswith, result):
        self.assertEqual(string.endswith(endswith), result)

    @parameterized.expand([
        ["", "", True],
        ["", ".", False],
    ])
    def test_endswith_boundary_value(self, string, endswith, result):
        self.assertEqual(string.endswith(endswith), result)

    @parameterized.expand([
        ["a/b/c", (
                "c",
                "/c",
                "b/c",
                "/b/c",
                "a/b/c",
        ), True],
        ["a/b/c", (
                "c/",
                "/c/",
                "b/c/",
                "/b/c/",
                "a/b/c/",
        ), False],
    ])
    def test_endswith_suffix_can_be_tuple(self, string, endswith, result):
        self.assertEqual(string.endswith(endswith), result)

    @parameterized.expand([
        ["a/b/c", ["list"], "list"],
        ["a/b/c", {"set"}, "set"],
        ["a/b/c", {"dict": "v"}, "dict"],
        ["a/b/c", True, "bool"],
        ["a/b/c", None, "NoneType"],
        ["a/b/c", 1, "int"],
    ])
    def test_endswith_suffix_type(self, string, endswith, suffix_type):
        with self.assertRaises(Exception) as context:
            string.endswith(endswith)
        self.assertEqual(
            "endswith first arg must be str or a tuple of str, not %s" % suffix_type,
            str(context.exception)
        )


if __name__ == '__main__':
    unittest.main()
