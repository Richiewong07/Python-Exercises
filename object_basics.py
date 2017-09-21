class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

    def greet(self, other_person):
        self.greeting_count += 1
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def print_contact_info(self):
        print("{0}'s email: {1}, {0}'s phone number: {2}".format(self.name, self.email, self.email))

    def add_friends(self, other_person):
        self.friends.append(other_person)

    def num_friends(self):
        return len(self.friends)



sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')


sonny.greet(jordan)
jordan.greet(sonny)

print(sonny.email, sonny.phone)
print(jordan.email, sonny.phone)




sonny.print_contact_info()
jordan.print_contact_info()

jordan.add_friends(sonny)
sonny.add_friends(jordan)

jordan.num_friends()
sonny.num_friends()



sonny.greeting_count

sonny.greet(jordan)
print(sonny.greeting_count)

sonny.greet(jordan)
print(onny.greeting_count)
