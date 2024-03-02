import json

try:
    favorite_number_file = "favorite_number.json"
    with open(favorite_number_file, "r") as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    pass
else:
    print(f"We know, your favorite number is {favorite_number}")


