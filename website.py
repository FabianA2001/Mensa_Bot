from flask import Flask
from Meals import Meals
import datetime

app = Flask("")


def generate_site():
    def headline(s):
        return f"<b>{s}</b><br>"

    def generate_string(date):
        def generate_substring(meals):
            result = ""
            for meal in meals:
                result += f"{meal.name}:<i>{meal.price}€</i><br>"
            return result

        string = ""

        meals = Meals(101, date)
        string += f"<h3>Mensa 1 am {date.strftime('%d.%m.%Y')}</h3>"
        string += headline("Hauptgericht")
        string += generate_substring(meals=meals.main_meal)
        string += headline("Beilage")
        string += generate_substring(meals=meals.supplement_meal)
        string += headline("Nachtisch")
        string += generate_substring(meals=meals.dessert_meal)
        return string

    def line():
        return "<hr><br><br><br><br>"

    string = "<br><br>"
    today = datetime.date.today()
    string += generate_string(today)
    string += line()
    string += generate_string(today + datetime.timedelta(days=1))
    string += line()
    string += generate_string(today + datetime.timedelta(days=2))
    string += line()
    string += generate_string(today + datetime.timedelta(days=3))
    return string


@app.route("/")
def home():
    return generate_site()


def run():
    app.run(host="localhost", port=8080)


run()
