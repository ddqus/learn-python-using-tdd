import unittest

from parameterized import parameterized


class MyTestCase(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
