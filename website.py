from flask import Flask
from Meals import Meals
import datetime

app = Flask("")


ids = {1: 101, 2: 105}


def generate_site(Mensa):
    def headline(s):
        return f"<b>{s}</b><br>"

    def generate_string(date, day=None):
        def generate_substring(meals):
            result = ""
            for meal in meals:
                result += f"{meal.name}:<i>{meal.price}€</i><br>"
            return result

        string = ""

        meals = Meals(ids[Mensa], date)
        if meals.main_meal == []:
            return ""

        if day == None:
            string += f"<h1>Mensa {Mensa} am {date.strftime('%d.%m.%Y')} ({date.strftime('%A')})</h1>"
        else:
            string += f"<h1>Mensa {Mensa} am {date.strftime('%d.%m.%Y')} ({day})</h1>"
        string += headline("Hauptgericht")
        string += generate_substring(meals=meals.main_meal)
        string += headline("Beilage")
        string += generate_substring(meals=meals.supplement_meal)
        string += headline("Nachtisch")
        string += generate_substring(meals=meals.dessert_meal)
        string += "<hr><br><br><br><br>"
        return string

    string = "<br><br>"
    today = datetime.date.today()
    for day in range(4):
        if day == 0:
            string += generate_string(today + datetime.timedelta(days=day), "Heute")
            continue
        if day == 1:
            string += generate_string(today + datetime.timedelta(days=day), "Morgen")
            continue
        string += generate_string(today + datetime.timedelta(days=day))

    return string


@app.route("/")
def home():
    return generate_site(1) + generate_site(2)


def run():
    app.run(host="localhost", port=8080)


run()
