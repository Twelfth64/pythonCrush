class Restaurant():

    def __init__(self, restraunt_name, cuisine_type):
        self.restraunt_name = restraunt_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restraunt(self):
        '''Shows restraunt attributes'''

        print(f"The restraunt called {self.restraunt_name}")
        print(f"Here is {self.cuisine_type} cusine is presented")

    def open_restaurant(self):
        '''Shows message about oppening the restraunt'''

        print("Rrestraunt is opened")

    def set_number_served(self, served):
        '''Set number of served tables'''

        self.number_served = served

    def get_number_served(self):
        '''Shows number of served tables'''

        return f"Currently {self.number_served} tables are served"

    def increment_number_served(self, served):
        '''Increment numbed of served tables to specified number'''
        if served > 0:
            self.number_served += served
        else:
            print("To decrement number of served tables use decrement_number_served method")


restaurant = Restaurant('Patriarshi', 'Asin')

print(restaurant.restraunt_name, restaurant.cuisine_type)
restaurant.describe_restraunt()
restaurant.open_restaurant()

print(restaurant.get_number_served())
restaurant.number_served = 2
print(restaurant.get_number_served())

restaurant.set_number_served(5)
print(restaurant.get_number_served())

restaurant.increment_number_served(-1)
print(restaurant.get_number_served())

restaurant.increment_number_served(5)
print(restaurant.get_number_served())


