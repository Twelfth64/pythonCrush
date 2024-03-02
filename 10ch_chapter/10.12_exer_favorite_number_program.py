import json


try:
    favorite_number_file = "favorite_number.json"
    with open(favorite_number_file, "r") as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    try:
        favorite_number_file = "favorite_number.json"
        favorite_number = int(input("Please enter your favorite number "))
    except ValueError:
        print("Please enter number")
    else:
        with open(favorite_number_file, 'w') as f:
            json.dump(favorite_number, f)
        print(f"We remember your favorite number is {favorite_number} and remind you when you back")
else:
    print(f"We know, your favorite number is {favorite_number}")
