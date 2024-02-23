class User:

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


class Admin(User):

    def __init__(self, first_name, last_name, gender, marriage_status):
        super().__init__(first_name, last_name, gender, marriage_status)
        self.privileges = ["alow add messages", "alow delete users", "alow ban users"]

    def show_privileges(self):
        print("As admin user has following priveleges:")
        for privelege in self.privileges:
            print(f"{privelege.title()}")


first_admin = Admin('Anatoly', 'Smirnov', 'Male', 'Not married')
first_admin.describe_user()
first_admin.show_privileges()

