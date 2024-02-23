class Privileges:

    def __init__(self):
        self.privileges = ["alow add messages", "alow delete users", "alow ban users"]

    def show_privileges(self):
        print("As admin user has following priveleges:")
        for privelege in self.privileges:
            print(f"{privelege.title()}")
