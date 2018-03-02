# class Dog():
#
#     # CLASS OBJECT ATTRIBUTE
#     # SAME FOR ANY INSTANCE OF A CLASS
#     species = 'mammal'
#
#     # FIRST METHOD OF THE  CLASS
#     # INIT: IS THE CONSTRUCTOR FOR THE CALL, CALLED AUTOMATICALLY WHEN YOU CREATE AN INSTANCE OF THE CLASS
#     # SELF: REPRESENTS INSTANCE OF THE OBJECT ITSELF
#     def __init__(self, breed, name):
#
#         # ATTRIBUTES: CHARACTERISTICS OF THE OBJECT
#         # WE TAKE IN THE ARGUEMENT
#         # ASSIGN IT USING self.attribute_name
#         self.breed = breed
#         self.name = name
#
#
#     # OPERATIONS/ACTIONS ---> METHODS
#     def bark(self, number):
#         print("WOOF! My name is {} and the number is {}".format(self.name, number))
#
# my_dog = Dog('Lab', 'Sammy')
#
# print(my_dog.bark(10))

class Circle():

    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self,radius = 1):
        self.radius = radius
        self.area = radius * radius * Circle.pi     # CLASS OBJECT ATTRIUTE CAN USE CLASS NAME INSTEAD OF SELF

    # METHOD
    def get_circumference(self):
        return self.radius * Circle.pi * 2      # CLASS OBJECT ATTRIUTE CAN USE CLASS NAME INSTEAD OF SELF

# INSTANCE
my_circle = Circle(30)

print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())

print(my_circle.area)
