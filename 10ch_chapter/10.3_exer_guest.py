
guest_name = str(input("Please enter your name "))

with open("guest.txt", "w") as guest_file:
    guest_file.write(guest_name)

