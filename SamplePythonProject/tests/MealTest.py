import unittest

from src.sample.Meal import *

class MealTest(unittest.TestCase):

    def setUp(self):
        self.tmp = Meal()

    def test_meal__id(self):
        self.assertEqual(self.tmp.meal__id(52772), "Teriyaki Chicken Casserole")

    def test_meal__name(self):
        self.assertEqual(self.tmp.meal__name("Arrabiata"), "Spicy Arrabiata Penne")




