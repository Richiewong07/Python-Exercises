class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # CLASS METHOD
    # NEED TO ADD DECORATOR
    # AUTOMATICALLY PASS cls
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # CLASS METHOD AS ALTERNATIVE CONSTRUCTOR
    # USUALLY STARTS WITH from
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')

        # USE CLASS VARIABLE --> CREATES NEW EMPLOYEE
        return cls(first, last, pay)

    # STATIC METHODS
    # DOES NOT AUTOMATICALLY PASS ANYTHING
    # DOES NOT DEPEND ON ANY INSTANCE OR CLASS VARIABLES
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Richie', 'Wong', 50000)
emp_2 = Employee('Test', 'User', 60000)


# HOW TO USE CLASS METHOD
Employee.set_raise_amount(1.05) # --> SAME AS Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_1.raise_amount)


# CLASS METHODS AS ALTERNATIVE CONSTRUCTORS --> USE CLASS METHODS TO PROVIDE MULTIPLE WAYS OF CREATING OUR OBJECTS

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

# USE OF STATIC METHODS
import datetime

my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))
