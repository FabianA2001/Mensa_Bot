from flask import Flask
from Meals import Meals

app = Flask("")


def headline(s):
    return f"<b>{s}</b><br>"


def generate_string():
    def generate_substring(meals):
        result = ""
        for meal in meals:
            result += f"{meal.name}:    {meal.price}€<br>"
        return result

    string = ""

    meals = Meals(101)
    string += "<h3>Mensa 1</h3>"
    string += headline("Hauptgericht")
    string += generate_substring(meals=meals.main_meal)
    string += headline("Beilage")
    string += generate_substring(meals=meals.supplement_meal)
    string += headline("Nachtisch")
    string += generate_substring(meals=meals.dessert_meal)
    return string


@app.route("/")
def home():
    return generate_string()


def run():
    app.run(host="localhost", port=8080)


run()
