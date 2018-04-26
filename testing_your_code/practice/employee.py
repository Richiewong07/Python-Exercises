class Employee():
    """A class to represent an employee"""
    def __init__(self, first, last, salary):
        self.first = first.title()
        self.last = last.title()
        self.salary = salary

    def give_raise(self, amount = 5000):
        self.salary += amount
