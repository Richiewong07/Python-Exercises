# Given the following code that prompts the user for a day number
# (the int function converts a numeric string to a number):

# The user will enter a number between 0 to 6 inclusive.
# Given this number, print a day of the week. 0 for Sunday, 1 for Monday, 2 for
# Tuesday, and so on.

input = int(input('Enter number for day of the week (0-6): '))

def conv_day(day):
    if day == 0:
        print('Sunday')
    elif day == 1:
        print('Monday')
    elif day == 2:
        print('Tuesday')
    elif day == 3:
        print('Wednesday')
    elif day == 4:
        print('Thursday')
    elif day == 5:
        print('Friday')
    elif day == 6:
        print('Saturday')


conv_day(input)
