import unittest

from parameterized import parameterized


class MyTestCase(unittest.TestCase):
    """
    https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy
    """

    def test___name__is_module_name(self):
        self.assertEqual(__name__, "test_predefined_attributes")

    def test___doc__is_none_when_documentation_is_not_exist(self):
        # TODO documentation 이 있는 경우도 테스트 해야함
        self.assertEqual(__doc__, None)

    def test_type_of___file___is_str(self):
        self.assertIsInstance(__file__, str)

    @parameterized.expand([
        ["learn-python-using-tdd", False],
        ["learn-python-using-tdd\\test", False],
        ["learn-python-using-tdd\\test\\datamodel", False],
        ["learn-python-using-tdd\\test\\datamodel\\test_predefined_attributes", False],
        ["learn-python-using-tdd\\test\\datamodel\\test_predefined_attributes.py", True],
    ])
    def test___file___is_fullpath(self, path, result):
        self.assertEqual(__file__.endswith(path), result)


if __name__ == '__main__':
    unittest.main()
