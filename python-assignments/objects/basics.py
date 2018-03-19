# 1. Basics

# Given the following Person class:

class Person:
    def __init__(self, name, email, phone, friend = [], greeting_list = []):
        self.name = name
        self.email = email
        self.phone = phone
        self.friend = friend
        self.greeting_list = greeting_list

    def greet(self, other_person):
        if other_person.name not in self.greeting_list:
            self.greeting_list.append(other_person.name)
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def unique_people_greeted(self):
        self.unique_people_greeted = len(self.greeting_list)
        print('Unique people greeted: {}'.format(self.unique_people_greeted))

    def print_contact_info(self):
        print(self.name, self.email, self.phone)

    def add_friend(self, other_person):
        self.friend.append(other_person)
        print('This is my friend, {}'.format(other_person.name))

    def num_friends(self):
        self.num_friend = len(self.friend)
        print('Friend count: {}'.format(self.num_friend))

    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)




# # Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
#
# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
#
# # Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
#
# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
#
# # Have sonny greet jordan using the greet method.
#
# sonny.greet(jordan)
#
# # Have jordan greet sonny using the greet method.
#
# jordan.greet(sonny)
#
# # Write a print statement to print the contact info (email and phone) of Sonny.
#
# print(sonny.email, sonny.phone)
#
# # Write another print statement to print the contact info of Jordan.
#
# print(jordan.email, jordan.phone)
#
# # Add a print_contact_info method to the Person class that will print out the contact info for a object instance of Person
#
# sonny.print_contact_info()
#
#
# # Implement an add_friend method to Person, so that in order to add a friend,
#
# jordan.add_friend(sonny)
#
#
# # Implement a num_friends method which returns the number of friends the person currently has:
#
# jordan.num_friends()
#
# # Count number of greetings
# # We want to count the number of times a person has greeted someone. To do this, we'll add another attribute, call it say greeting_count, and initialize it to 0. Then each time the greet method is called, we'll increment greeting_count by 1.
#
# jordan.greet(sonny)
# jordan.greeting_count
#
#
# # Implement your own __str__ method, and you can represent your person objects however you want. Incidentally, __str__ is also used when you use convert your object to a string: str(jordan).
#
# print(jordan)


# Bonus Challenge
# Keep track of the number of unique people a person has greeted, and be able to report that number via the num_unique_people_greeted method:

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
ann = Person('Ann', 'ann@aol.com', '111-111-1111')
richie = Person('Richie', 'richiewong07@yahoo.com', '281-702-7171')

jordan.greet(sonny)
jordan.greet(ann)
jordan.greet(richie)


jordan.unique_people_greeted()
