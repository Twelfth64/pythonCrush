
with open("learning_python.txt") as file:
    print(file.read())

with open("learning_python.txt") as file:
    lines = file.readlines()
    print(lines)

with open("learning_python.txt") as file:
    some_list = []
    for line in file.readlines():
        some_list.append(line)

    print(some_list)
