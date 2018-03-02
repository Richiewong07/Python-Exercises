class Dog():

    def __init__(self, breed, name, spots):

        # ATTRIBUTES
        # WE TAKE IN THE ARGUEMENT
        # ASSIGN IT USING self.attribute_name
        self.breed = breed
        self.name = name

        # EXPECT A BOOLEAN T/F
        self.spots = spots

my_dog = Dog(breed = 'Lab', name = 'Sammy', spots = 'False')

print(type(my_dog))

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
