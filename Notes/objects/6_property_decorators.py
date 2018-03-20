class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@email.com'

    # PROPERTY DECORATOR --> ALLOWS TO ACCESS METHODS LIKE PROPERTIES
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # SETTER DECORATOR
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # DELETER DECORATOR
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith')

# WANT TO CHANGE EMAIL WHEN NAME IS CHANGE --> PROPERTY DECORATOR
emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email) # () IS TAKEN OFF

# WANT TO CHANGE FIRST NAME, LAST NAME, AND EMAIL WHEN FULLNAME IS CHANGE --> SETTER DECORATOR
emp_1.fullname = 'Richie Wong'
print(emp_1.fullname)

# WHEN YOU WANT TO DELETE AND ATTRIBUTE --> DELETER DECORATOR
del emp_1.fullname
