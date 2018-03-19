
class Employee:

    # INIT METHOD OR CONSTRUCTOR METHOD
    # INIT METHOD TAKES INSTANCE AS SELF
    def __init__(self, first, last, pay):

        # ATTRIBUTES OF THE CLASS
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # METHOD WITHIN OUR CLASS
    # AUTOMATICALLY TAKES INSTANCES (self) AS IT'S FIRST ARGUEMENT
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# emp_1 and emp_2 ARE INSTANCES OF THE CLASS AND PASS TO self
emp_1 = Employee('Richie', 'Wong', 50000)
emp_2 = Employee('Test', 'User', 60000)


# NEED TO ADD () TO RUN METHODS, AUTOMATICALLY PASSES IN self
print(emp_1.fullname())
print(emp_2.fullname())


# HOW TO RUN METHODS USING CLASS NAME
# HAVE TO MANUALLY PASS IN INSTANCES AS AN ARGUMENT
print(Employee.fullname(emp_1))


# HOW TO SET INSTANCE VARIABLES
# emp_1.first = 'Richie'
# emp_1.last = 'Wong'
# emp_1.email = 'richiewong07@yahoo.com'
# emp_1.pay = 6000
