from Meals import Meals

# from google_images import search


def show(meals):
    print("Main:")
    for main in meals.main_meal:
        print("    ", main.name, end=":")
        print(main.price, "€")
    print("Beilage:")
    for sub in meals.supplement_meal:
        print("    ", sub.name, end=":")
        print(sub.price, "€")

    print("Nachtisch:")
    for des in meals.dessert_meal:
        print("    ", des.name, end=":")
        print(des.price, "€")


if __name__ == "__main__":
    print("run Discord.py")  # cant change the structure of discord.py

    # meals = Meals()
    # show(meals)
