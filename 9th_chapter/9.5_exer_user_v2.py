
class User():

    def __init__(self, first_name, last_name, gender, marriage_status):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.marriage_status = marriage_status
        self.login_attempts = 0

    def greet_user(self):
        '''Greets the user'''

        print(f"Hello {self.first_name.title()}")

    def describe_user(self):
        '''Describes user'''

        print(f"User full name is {self.first_name.title()} {self.last_name.title()}")
        print(f"User is {self.gender.lower()} and {self.marriage_status.lower()}")

    def get_login_attempts(self):
        return self.login_attempts

    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0

first_user = User('Antonio', 'Padaleki', 'Male', 'Maried')
second_user = User('Paula', 'De-puchi', 'Female', 'Not maried')

first_user.greet_user()
first_user.describe_user()

second_user.greet_user()
second_user.describe_user()

first_user.increment_login_attempts()
first_user.increment_login_attempts()

print(first_user.get_login_attempts())

first_user.reset_login_attempts()
print(first_user.get_login_attempts())

