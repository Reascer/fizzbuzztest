import unittest
from fizzbuzz import FizzBuzz

class Casetest(unittest.TestCase):
    def test_should_raise_error_with_0(self):
        with self.assertRaises(ValueError):
            FizzBuzz(0)

    def test_should_raise_error_with_negative_number(self):
        with self.assertRaises(ValueError):
            FizzBuzz(-5)

if __name__ == '__main__':
    unittest.main()