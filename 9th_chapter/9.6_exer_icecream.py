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


class IceCreamStand(Restaurant):

    def __init__(self, restraunt_name, cuisine_type, *flavors):
        super().__init__(restraunt_name, cuisine_type)
        self.flavors = flavors


    def get_flavors_list(self):
        print(f"Now we have following flavors {self.flavors}")


first_icecream_stand = IceCreamStand('Hachipuri', 'Georgian', 'Carbonara', 'Orange', 'Apple')
first_icecream_stand.get_flavors_list()

