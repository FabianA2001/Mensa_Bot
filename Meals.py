import requests
import datetime


class Meal:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class Meals:
    def __init__(self) -> None:
        self.main_meal = []
        self.supplement_meal = []
        self.dessert_meal = []
        self.get_data()

    def get_data(self):
        respond = requests.get(
            # url=f"https://sls.api.stw-on.de/v1/location/101/menu/{datetime.date.today()}"
            url=f"https://sls.api.stw-on.de/v1/location/101/menu/2022-10-11"
        )
        meals = respond.json()["meals"]

        for meal in meals:
            if (meal["lane"]["id"]) in [90]:
                self.dessert_meal.append(Meal(meal["name"], meal["price"]["student"]))
            elif (meal["lane"]["id"]) in [160, 110]:
                self.supplement_meal.append(
                    Meal(meal["name"], meal["price"]["student"])
                )
            else:
                self.main_meal.append(Meal(meal["name"], meal["price"]["student"]))


if __name__ == "__main__":
    x = Meals()
    print(x.get_data())
