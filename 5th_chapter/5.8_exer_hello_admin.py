names = ['Sergei', 'admin', 'Madina', 'Herk', 'Gorg']

if names:
    for name in names:
        if name == 'admin':
            print(f"Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {name}, thank you for logging in again")
else:
    print("We need to ind some users!")
