
while True:
    guest_name = str(input("Please enter your name. Enter 'q' to quit "))
    if guest_name == "q":
        break
    else:
        with open("guest_book.txt", "a") as guest_book:
            guest_book.write(guest_name + "\n")
