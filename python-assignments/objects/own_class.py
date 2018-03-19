# 2. Make your own class
# Create a class Vehicle. A Vehicle object will have 3 attributes:
#
# make
# model
# year

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.make, self.model, self.year)

car = Vehicle('Nissian', 'Leaf', 2015)

# Add a print_info method to the Vehicle class. It will print out the vehicle's information like so:

car.print_info()
