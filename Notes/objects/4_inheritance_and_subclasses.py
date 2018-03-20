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


# SUBCLASS
class Developer(Employee):

    # RAISED AMOUNT CHANGE FOR DEVELOPER CLASS
    raise_amount = 1.10

    # HOW TO ADD ADDITIONAL ATTRIBUTES
    def __init__(self, first, last, pay, prog_lang):

        # super ALLOWS TO PASS THESE ATTRIBUTES TO THE EMPLOYEE INIT METHOD
        # OR --> Employee.__init__(self, first, last, pay)
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    # NEVER WANT TO PASS MUTABLE DATA
    # WANT TO PASS NONE INSTEAD OF A LIST OR DICT
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())    # fullname() METHOD FROM PARENT CLASS

# CAN ACCESS ATTRIBUTES MADE IN PARENT CLASS
# METHOD RESOLUTION ORDER --> GOES UP INHERITANCE CHAIN
# CAN ADD NEW ATTRIBUTES IN SUBCLASS
dev_1 = Developer('Richie', 'Wong', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

# print(dev_1.email)
# print(dev_1.prog_lang)


# HOW TO LOOK UP METHOD RESOLUTION ORDER
# SHOW METHODS INHERITED
# print(help(Developer))

# RAISED AMOUNT CHANGE FOR DEVELOPER CLASS BUT NOT FOR EMPLOYEE CLASS
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)


# TEST MANAGER SUBCLASS
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.print_emps()
# mgr_1.remove(dev_1)


# PYTHON BUILTIN FUNCTIONS
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee))
