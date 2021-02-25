import unittest
from fizzbuzz import FizzBuzz

class Casetest(unittest.TestCase):
    def test_should_raise_error_with_0(self):
        with self.assertRaises(ValueError):
            FizzBuzz(0)

    def test_should_raise_error_with_negative_number(self):
        with self.assertRaises(ValueError):
            FizzBuzz(-5)

    def test_should_return_fizz_if_numbre_is_multple_of_3(self):
        exp = "fizz"
        actual = FizzBuzz(18)
        self.assertEqual(exp, actual, "Should be fizz")
    
    def test_should_return_buzz_if_numbre_is_multple_of_5(self):
        exp = "buzz"
        actual = FizzBuzz(20)
        self.assertEqual(exp, actual, "Should be buzz")
    
    def test_should_return_fizzbuzz_if_numbre_is_multple_of_3_and_5(self):
        exp = "fizzbuzz"
        actual = FizzBuzz(75)
        self.assertEqual(exp, actual, "Should be fizzbuzz")

if __name__ == '__main__':
    unittest.main()