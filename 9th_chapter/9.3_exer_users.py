
class User():

    def __init__(self, first_name, last_name, gender, marriage_status):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.marriage_status = marriage_status

    def greet_user(self):
        '''Greets the user'''

        print(f"Hello {self.first_name.title()}")

    def describe_user(self):
        '''Describes user'''

        print(f"User full name is {self.first_name.title()} {self.last_name.title()}")
        print(f"User is {self.gender.lower()} and {self.marriage_status.lower()}")

first_user = User('Antonio', 'Padaleki', 'Male', 'Maried')
second_user = User('Paula', 'De-puchi', 'Female', 'Not maried')

first_user.greet_user()
first_user.describe_user()

second_user.greet_user()
second_user.describe_user()

