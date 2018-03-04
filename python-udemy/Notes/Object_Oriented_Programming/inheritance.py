# BASE CLASS
class Animal():

    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

myanimal = Animal()

print(myanimal.who_am_i(), myanimal.eat())


# DERIVED CLASS
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')

    # CAN OVERRIGHT METHOD
    def who_am_i(self):
        print('I am a dog!')

    # CAN ADD METHOD
    def bark(self):
        print('WOOF!')

mydog = Dog()
print(mydog)
print(mydog.who_am_i(), mydog.eat(), mydog.bark())
