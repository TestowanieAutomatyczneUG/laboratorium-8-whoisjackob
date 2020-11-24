import unittest
from sample.Meal import *

class RomanParameterizedFile(unittest.TestCase):

    def test_from_file(self):
        fileTest = open("data/roman_data_test")
        tmpRoman = Roman()
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp, result = int(data[0]), data[1].strip("\n")
                self.assertEqual(tmpRoman.roman(inp), result)
        fileTest.close()


if __name__ == '__main__':
    unittest.main()
