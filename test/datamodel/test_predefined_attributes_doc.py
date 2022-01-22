"""
this is module doc
"""
import unittest


class MyTestCase(unittest.TestCase):
    """
    this is pydoc
    """

    def test___doc__is_exist(self):
        self.assertEqual(__doc__, "\nthis is module doc\n")


if __name__ == '__main__':
    unittest.main()
