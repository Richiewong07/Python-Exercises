class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # USED FOR DEBUGGING AND LOGGING --> FOR DEVELOPERS
    # WANT TO RETURN SOMETHING TO RECREATE THE OBJECT
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    # READABLE DISPLAY OF THE OBJECT --> FOR END USERS
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Richie', 'Wong', 50000)
emp_2 = Employee('Test', 'User', 60000)


# ALLOWS US TO CHANGE HOW THE OBJECT IS DISPLAYED
print(repr(emp_1)) # --> SAME AS print(emp_1.__repr__())
print(str(emp_1))  # --> SAME AS print(emp_1.__str__())


# THUNDER ADD METHOD
print(emp_1 + emp_2) # --> SAME AS print(emp_1.pay + emp_2.pay)


# THUNDER LEN METHOD
print(len(emp_1)) # --> SAME AS print(len(emp_1.fullname()))


# OTHER SPEICAL METHODS EXAMPLES
# print(int.__add__(1,2))
# print(str.__add__('a', 'b'))
# print('test'.__len__())
