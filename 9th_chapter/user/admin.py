from .user import User
from .privileges import Privileges


class Admin(User):

    def __init__(self, first_name, last_name, gender, marriage_status):
        super().__init__(first_name, last_name, gender, marriage_status)
        self.privileges = Privileges()

