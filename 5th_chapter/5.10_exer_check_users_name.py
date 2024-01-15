current_users = ['Sergei', 'admin', 'Madina', 'Herk', 'Gorg']
new_users = ['SERGEI', 'Jhon', 'MaDiNa', 'Elen', 'Herk']

current_users_lower = []
for current_user in current_users:
    current_users_lower.append(current_user.lower())

if new_users:
    for new_user in new_users:
        if new_user.lower() in current_users_lower:
            print(f"{new_user} name is used already, please choose another name")
        else:
            print(f"{new_user} name is available")