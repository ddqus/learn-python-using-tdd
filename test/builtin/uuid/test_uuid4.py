import unittest
from uuid import UUID


class MyTestCase(unittest.TestCase):
    _orig_hex_val = "491310b4-5a49-483e-0000-836dc7719690"
    _fixed_hex_val = "491310b4-5a49-483e-8000-836dc7719690"
    _fixed_int_val = 97132636140176175073288884668458964624
    _fixed_int_val2 = 97132636140176175064065512631604188816

    def test_ver4_can_change_hex(self):
        u1 = UUID(self._orig_hex_val, version=4)
        self.assertNotEqual(hex, str(u1))
        self.assertEqual(self._fixed_hex_val, str(u1))

    def test_ver4_hex_and_int(self):
        u1 = UUID(self._fixed_hex_val, version=4)
        self.assertEqual(self._fixed_int_val, u1.int)

        u2 = UUID(int=self._fixed_int_val, version=4)
        self.assertEqual(self._fixed_hex_val, str(u2))

    def test_ver4_unknown(self):
        self.assertNotEqual(
            self._fixed_int_val,
            self._fixed_int_val2,
        )
        self.assertEqual(9223372036854775808, self._fixed_int_val - self._fixed_int_val2)

        # 다른 int 로 생성을 했는데 동일한 str 이 생성된다
        self.assertEqual(
            str(UUID(int=self._fixed_int_val, version=4)),
            str(UUID(int=self._fixed_int_val2, version=4)),
        )

    def test_ver4_2(self):
        u1 = UUID(int=self._fixed_int_val, version=4)
        u2 = UUID(int=self._fixed_int_val2, version=4)
        self.assertEqual(u1.hex, u2.hex)
        self.assertEqual(u1.urn, u2.urn)
        self.assertEqual(u1.bytes, u2.bytes)


if __name__ == '__main__':
    unittest.main()
