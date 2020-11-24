import requests

class Meal:
    def meal__id(self, id_value):
        if type(id_value) != int and type(id_value) != str:
            raise TypeError("Podaj właściwy format")

        meal = requests.get(f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={id_value}').json()
        return meal["meals"][0]["strMeal"]

    def meal__name(self, name_value):
        if type(name_value) != str:
            raise TypeError("Podaj właściwy format")

        meal = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={name_value}').json()
        return meal["meals"][0]["strMeal"]

    def random_meal(self):
        return requests.get('https://www.themealdb.com/api/json/v1/1/random.php').json()

    def meal_letter(self, letter):
        if type(letter) != str:
            raise TypeError("Podaj właściwy format")

        meal = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?f={letter}').json()
        return meal["meals"][0]

    def meal_ingr(self, ingr):
        if type(ingr) != str:
            raise TypeError("Podaj właściwy format")

        meal = requests.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?i={ingr}').json()
        return meal["meals"][0]


