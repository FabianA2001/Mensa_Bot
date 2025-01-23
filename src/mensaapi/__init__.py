from flask import Flask
from .Meals import Meals
import datetime


app = Flask("")
ids = {1: 102, 2: 105}
day_names = {"Monday":"Montag", "Tuesday":"Dienstag", "Wednesday" : "Mittwoch", "Thursday":"Donnerstag", "Friday":"Freitag"}


def generate_site(Mensa):
    def headline(s):
        return f"<b>{s}</b><br>"

    def generate_string(date, day=None):
        def generate_substring(meals, displayTime=False):
            result = ""
            for meal in meals:
                if(displayTime):
                    result += f"{meal.name}:<i>{meal.price}€</i> {meal.time}<br>"
                else:
                    result += f"{meal.name}:<i>{meal.price}€</i><br>"
            return result

        string = ""
        meals = Meals(ids[Mensa], date)
        if meals.main_meal == []:
            return ""

        meals.main_meal.sort();

        if day == None:
            string += f"<h1>Mensa {Mensa} am {date.strftime('%d.%m.%Y')} ({day_names[date.strftime('%A')]})</h1>"
        else:
            string += f"<h1>Mensa {Mensa} am {date.strftime('%d.%m.%Y')} ({day_names[day]})</h1>"
        string += headline("Hauptgericht")
        string += generate_substring(meals=[i for i in meals.main_meal if i.time == "noon"])
        string += headline("Beilage")
        string += generate_substring(meals=meals.supplement_meal)
        string += headline("Nachtisch")
        string += generate_substring(meals=meals.dessert_meal)
        if("evening" in [i.time for i in meals.main_meal]):
            string += headline("Abends")
            string += generate_substring(meals=[i for i in meals.main_meal if i.time == "evening"])
        string += "<hr><br><br><br><br>"
        return string

    string = "<br><br>"
    today = datetime.date.today()
    for day in range(6):
        string += generate_string(today + datetime.timedelta(days=day))

    return string


@app.route("/")
def home():
    return generate_site(1) + generate_site(2)

def main():
    app.run(host="0.0.0.0", port=8080)

