
while True:
    try:
        print("Please enter first number")
        print("Enter 'q' to quit")
        first_number = int(input())
        if first_number == 'q':
            break
        print("Please enter second number")
        print("Enter 'q' to quit")
        second_number = int(input())
        if second_number == 'q':
            break
    except ValueError:
        print("Please enter only numbers")
    else:
        print(first_number + second_number)

