import unittest
import app


class MyTestCase(unittest.TestCase):
    def test_init(self):
        self.assertEqual(app.dummy_for_test(), "app")


if __name__ == '__main__':
    unittest.main()
