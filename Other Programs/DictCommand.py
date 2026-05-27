import json
from datetime import datetime

# Full-featured car dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "specs": {
        "engine": "V8",
        "horsepower": 271,
        "transmission": "manual",
        "top_speed_mph": 120,
    },
    "owners": [{"name": "Alice", "since": 1965}, {"name": "Bob", "since": 1972}],
}

def print_dict(d):
    print(json.dumps(d, indent=4))


def car_age(car):
    current_year = datetime.now().year
    return current_year - car["year"]


def add_owner(car, name, since):
    car["owners"].append({"name": name, "since": since})


def update_specs(car, key, value):
    car["specs"][key] = value


def owners_after(car, year):
    return [owner for owner in car["owners"] if owner["since"] > year]


def display_car_info(car):
    engine = car["specs"]["engine"]
    hp = car["specs"]["horsepower"]
    age = car_age(car)
    newest_owner = car["owners"][-1]["name"] if car["owners"] else "None"

    print(f"{car['brand']} {car['model']} ({car['year']})")
    print(f"Engine: {engine}, Horsepower: {hp} HP")
    print(f"Age: {age} years")
    print(f"Newest Owner: {newest_owner}")
    print(f"Total Owners: {len(car['owners'])}\n")


thisdict["year"] = 2023

update_specs(thisdict, "top_speed_mph", 155)

add_owner(thisdict, "Charlie", 2024)
add_owner(thisdict, "Dana", 2025)

display_car_info(thisdict)

recent_owners = owners_after(thisdict, 2000)
print("Owners since 2000:")
for owner in recent_owners:
    print(f"- {owner['name']} (since {owner['since']})")

print("\nFull car details:")
print_dict(thisdict)
