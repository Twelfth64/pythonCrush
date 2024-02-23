from user.admin import Admin

my_admin = Admin('Anatoly', 'Smirnov', 'Male', 'Not married')

my_admin.describe_user()
my_admin.privileges.show_privileges()


