class Restaurant():

    def __init__(self, restraunt_name, cuisine_type):
        self.restraunt_name = restraunt_name
        self.cuisine_type = cuisine_type

    def describe_restraunt(self):
        '''Shows restraunt attributes'''

        print(f"The restraunt called {self.restraunt_name}")
        print(f"Here is {self.cuisine_type} cusine is presented")

    def open_restaurant(self):
        '''Shows message about oppening the restraunt'''

        print("Rrestraunt is opened")


asian_restaurant = Restaurant('Patriarshi', 'Asian')
street_food_restaurant = Restaurant('MySoso', 'Streetfood')
italian_restraunt = Restaurant('Bonuchi', 'Italian')

asian_restaurant.describe_restraunt()
street_food_restaurant.describe_restraunt()
italian_restraunt.describe_restraunt()

