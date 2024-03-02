
try:
    with open("dogs.txt", "r") as f:
        print(f.read())

    with open("cats.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    pass

