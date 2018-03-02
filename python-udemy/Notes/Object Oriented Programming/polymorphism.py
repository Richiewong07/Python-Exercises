# class Dog():
#
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return self.name + " says woof!"
#
#
# class Cat():
#
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return self.name + " says meow!"
#
#
# nikko = Dog('Niko')
# felix = Cat('Felix')
#
# # print(nikko.speak())
# # print(felix.speak())
#
#
# # for pet in [nikko, felix]:
# #
# #     print(type(pet))
# #     print(pet.speak())
#
# def pet_speak(pet):
#     print(pet.speak())
#
# print(pet_speak(nikko))
# print(pet_speak(felix))



class Animal():

    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abtract method")

# print(myanimal.speak())

class Dog(Animal):

    def speak(self):
        return self.name + " says woof!"

class Cat(Animal):

    def speak(self):
        return self.name + " says meow!"

fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak(), isis.speak())
