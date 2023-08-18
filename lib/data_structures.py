spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
   food_names = [food['name'] for food in spicy_foods]
   return food_names

def get_spiciest_foods(spicy_foods):
    spiciest = [food for food in spicy_foods if (food["heat_level"] > 5)]
    return spiciest

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        food_name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "**" * food["heat_level"]
        print(f"{food_name} ({cuisine}) | heat level: {heat_level}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            food_name = food["name"]
            cuisine = food["cuisine"]
            heat_level = food["heat_level"]
            print(f"{food_name} ({cuisine}) | heat level: {heat_level}")

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    number_of_foods = len(spicy_foods)
    return total_heat_level/number_of_foods

def create_spicy_food(spicy_foods, spicy_food):
    pass
