try:
    print("Please enter first number")
    first_number = int(input())
    print("Please enter second number")
    second_number = int(input())
except ValueError:
    print("Please enter only numbers")
else:
    print(first_number + second_number)

