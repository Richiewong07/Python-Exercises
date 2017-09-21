class Person:
   def __init__ (self, age):
       self.name = name
       #self.age = age
   def greet (self, friend):
    #    if friend.age < 30:
    #       print('Hi')
    #    else:
          print("Hello {} and {}".format(self.name, friend.name))

me = Person('Richie')
me.greet('Timmy')

# class Person:
#   feet = 2
#   def __init__ (self, name):
#     self.name = name
#   @classmethod
#   def create (cls):
#     name = input('What is your name? ')
#     return cls(name)
#   @staticmethod
#   def fix_name (name):
#     return name.replace('-', ' ')
#
# me = Person.create()
# Person.fix_name('hello-you')
# me = Person(Person.fix_name('Richie'))
