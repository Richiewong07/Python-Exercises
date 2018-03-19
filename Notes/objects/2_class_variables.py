class Employee:

    # CLASS VARIABLES ARE THE SAME FOR EACH INSTANCES
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # USE CLASS INSTEAD OF SELF B/C THERE IS NO NEED TO OVERRIDE
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # NEED TO ACCESS CLASS VARIABLE THROUGH CLASS ITSELF --> Employee.raise_amount OR INSTANCE OF THE CLASS --> self.raise_amount
    # USING self LETS YOU CHANGE AMOUNT FOR SINGLE INSTANCE IF WANTED TOO (SUBCLASS OVERRIDES CONSTANT)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Richie', 'Wong', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps)


# FIRST CHECKS IF INSTANCE CONTAINS THAT ATTRIBUTE
# THEN CHECKS CLASS OR CLASS IT INHERITS FROM CONTAINS THAT ATTRIBUTE
# print(emp_1.__dict__)
# print(Employee.__dict__)


# WILL CHANGE VALUE FOR CLASS AND ALL THE INSTANCES
# Employee.raise_amount = 1.05


# WILL ONLY CHANGE ATTRIBUTE FOR INSTANCE
# WILL ALSO GIVE ATTRIBUTE TO THE NAMESPACE
# emp_1.raise_amount = 1.05
