import json


def check_username(username):
    """Ask user is the name right or not"""
    try:
        user_answer = str(input(f"Is {username} your name? (y/n) "))
        if user_answer.lower() == 'y':
            return True
        elif user_answer.lower() == 'n':
            return False
    except ValueError:
        return check_username(username)


def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
        return username


def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
        if check_username(username):
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
    else:
        username = get_new_username()


greet_user()
