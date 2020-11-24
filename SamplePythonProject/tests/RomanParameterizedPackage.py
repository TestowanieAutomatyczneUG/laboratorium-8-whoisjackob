import unittest
from sample.Meal import *
from parameterized import parameterized, parameterized_class
import math

class RomanParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Roman()

    @parameterized.expand([
        (1, "I"),
        (2, "II"),
        (3, "III"),
    ])
    def test_one_parameterized(self,number, expected):
        self.assertEqual(self.tmp.roman(number), expected)


@parameterized_class(('number', 'expected'), [
        (1, "I"),
        (2, "II"),
        (3, "III"),
])
class RomanParameterizedPackage2(unittest.TestCase):
    def setUp(self):
        self.tmp = Roman()

    def test_second_parameterized(self):
        self.assertEqual(self.tmp.roman(self.number), self.expected)


if __name__ == '__main__':
    unittest.main()
