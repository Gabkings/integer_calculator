import unittest
from bigint_calculator import BigInt 

class TestBigInt(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(str(BigInt("123456789") + BigInt("987654321")), "1111111110")
        self.assertEqual(str(BigInt("-123456789") + BigInt("123456789")), "0")
        self.assertEqual(str(BigInt("0") + BigInt("0")), "0")

    def test_subtraction(self):
        self.assertEqual(str(BigInt("1000000") - BigInt("1")), "999999")
        self.assertEqual(str(BigInt("123456789") - BigInt("987654321")), "-864197532")
        self.assertEqual(str(BigInt("-123456789") - BigInt("-987654321")), "864197532")

    def test_multiplication(self):
        self.assertEqual(str(BigInt("123456789") * BigInt("987654321")), "121932631112635269")
        self.assertEqual(str(BigInt("-123456789") * BigInt("987654321")), "-121932631112635269")
        self.assertEqual(str(BigInt("0") * BigInt("123456789")), "0")

    def test_division(self):
        self.assertEqual(str(BigInt("987654321") / BigInt("123456789")), "8")
        self.assertEqual(str(BigInt("123456789") / BigInt("987654321")), "0")
        self.assertEqual(str(BigInt("-987654321") / BigInt("123456789")), "-8")

    def test_modulo(self):
        self.assertEqual(str(BigInt("987654321") % BigInt("123456789")), "9")
        self.assertEqual(str(BigInt("123456789") % BigInt("987654321")), "123456789")
        self.assertEqual(str(BigInt("123456789") % BigInt("-987654321")), "123456789")

    def test_exponentiation(self):
        self.assertEqual(str(BigInt("2") ** BigInt("10")), "1024")
        self.assertEqual(str(BigInt("5") ** BigInt("0")), "1")
        self.assertEqual(str(BigInt("1") ** BigInt("10000")), "1")

    def test_factorial(self):
        self.assertEqual(str(BigInt("0").factorial()), "1")
        self.assertEqual(str(BigInt("1").factorial()), "1")
        self.assertEqual(str(BigInt("5").factorial()), "120")
        self.assertEqual(str(BigInt("10").factorial()), "3628800")

    def test_compare(self):
        self.assertTrue(BigInt._compare("123456789", "987654321") < 0)
        self.assertTrue(BigInt._compare("987654321", "123456789") > 0)
        self.assertTrue(BigInt._compare("123456789", "123456789") == 0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            BigInt("abc")
        with self.assertRaises(ValueError):
            BigInt("--123")

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            BigInt("123456789") / BigInt("0")
        with self.assertRaises(ZeroDivisionError):
            BigInt("123456789") % BigInt("0")

if __name__ == "__main__":
    unittest.main()
