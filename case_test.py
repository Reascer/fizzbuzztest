from fizzbuzz import FizzBuzz
import unittest

class Casetest(unittest.TestCase):
    def test_should_raise_error(self):
        with self.assertRaises(ValueError):
            FizzBuzz(5)

if __name__ == '__main__':
    unittest.main()