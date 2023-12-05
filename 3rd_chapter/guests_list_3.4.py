# list of guests
dinner_guests = ['Madina', 'Ariana', 'Mars', 'Askar']

for guest in dinner_guests:
    print(f'Deer {guest}, I\'m glad to invite you to my dinner')

print(f'''\nUnfortunately {dinner_guests.pop()} can\'t come \n''')
dinner_guests.append('Aleks')

for guest in dinner_guests:
    print(f'Deer {guest}, I\'m glad to invite you to my dinner')

print('\nNew guests are invited to dinner\n')
dinner_guests.insert(0, 'Solo')
dinner_guests.insert(2, 'Lola')
dinner_guests.append('Cristian')

for guest in dinner_guests:
    print(f'Deer {guest}, I\'m glad to invite you to my dinner')

print('\nUnfortunately only 2 guest are invited, because my table is getting late.\n')

for i in range(len(dinner_guests)):
    if len(dinner_guests) != 2:
        removed_guest = dinner_guests.pop()
        print(f'''Dear {removed_guest}, I'm sorry to say it, but we can't meet this time.
See you next time. Good luck!''')
    else:
        print('\n')
        break

for guest in dinner_guests:
    print(f'Deer {guest}, I\'m letting you know you are still invited to dinner')

for i in range(len(dinner_guests)):
    del dinner_guests[0]

print('\n')
print(dinner_guests)
