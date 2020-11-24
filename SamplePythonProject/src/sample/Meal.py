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
