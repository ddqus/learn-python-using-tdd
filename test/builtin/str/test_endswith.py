import unittest


class MyTestCase(unittest.TestCase):
    def test_endswith(self):
        self.assertEqual("a/b/c".endswith("c"), True)
        self.assertEqual("a/b/c".endswith("/c"), True)
        self.assertEqual("a/b/c".endswith("b/c"), True)
        self.assertEqual("a/b/c".endswith("/b/c"), True)
        self.assertEqual("a/b/c".endswith("a/b/c"), True)

        self.assertEqual("a/b/c".endswith("c/"), False)
        self.assertEqual("a/b/c".endswith("/c/"), False)
        self.assertEqual("a/b/c".endswith("b/c/"), False)
        self.assertEqual("a/b/c".endswith("/b/c/"), False)
        self.assertEqual("a/b/c".endswith("a/b/c/"), False)


if __name__ == '__main__':
    unittest.main()
