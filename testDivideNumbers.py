""" Test our divideTwoNumbers function"""

import unittest

from divideNumbers import divideTwoNumbers

class TestDivideNumbers(unittest.TestCase):
    """Test divideNumbers functionality"""
    def test_is_an_integer(self):
        type(self) == int
    def test_division(self):
        self.assertEqual(divideTwoNumbers(6, 2), 3)
        self.assertEqual(divideTwoNumbers(-3, 1), -3)
        self.assertEqual(divideTwoNumbers(7,2), 3.5)
    def test_raises_exception(self):
        with self.assertRaises(ValueError):
            divideTwoNumbers(4,0)

if __name__ == '__main__':
    unittest.main()
