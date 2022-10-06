from Meals import Meals


def show(meals):
    print("Main:")
    for main in meals.main_meal:
        print("    ", main)
    print("Beilage:")
    for sub in meals.supplement_meal:
        print("    ", sub)
    print("Nachtisch:")
    for des in meals.dessert_meal:
        print("    ", des)


if __name__ == "__main__":
    meals = Meals()
    show(meals)
