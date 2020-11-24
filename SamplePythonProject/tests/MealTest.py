import unittest
import requests

from src.sample.Meal import *

class MealTest(unittest.TestCase):

    def setUp(self):
        self.tmp = Meal()

    def test_meal__id(self):
        self.assertEqual(self.tmp.meal__id(52772), "Teriyaki Chicken Casserole")

    def test_meal__name(self):
        self.assertEqual(self.tmp.meal__name("Arrabiata"), "Spicy Arrabiata Penne")

    def test_meal__letter_id(self):
        self.assertEqual(self.tmp.meal_letter("b")["idMeal"], "52767")

    def test_meal__letter_category(self):
        self.assertEqual(self.tmp.meal_letter("d")["strCategory"], "Vegetarian")

    def test_meal__letter_area(self):
        self.assertEqual(self.tmp.meal_letter("e")["strArea"], "British")

    def test_meal__letter_str(self):
        self.assertEqual(self.tmp.meal_letter("c")["strMeal"], "Chocolate Gateau")

    def test_meal_ingr(self):
        self.assertEqual(self.tmp.meal_ingr("chicken_breast")["strMeal"], "Chick-Fil-A Sandwich")


    ["strMeal"]

    #def test_random_meal(self):
    #    self.assertEqual(self.tmp.random_meal(), requests.get('https://www.themealdb.com/api/json/v1/1/random.php').json())




