import requests
import datetime


class Meals:
    def __init__(self) -> None:
        self.main_meal = []
        self.supplement_meal = []
        self.dessert_meal = []
        self.get_data()

    def get_data(self):
        respond = requests.get(
            url=f"https://sls.api.stw-on.de/v1/location/101/menu/{datetime.date.today()}"
        )
        meals = respond.json()["meals"]

        for meal in meals:
            if (meal["lane"]["id"]) in [90]:
                self.dessert_meal.append(meal["name"])
            elif (meal["lane"]["id"]) in [160, 110]:
                self.supplement_meal.append(meal["name"])
            else:
                self.main_meal.append(meal["name"])
