# Prompt the user for a day of the week just like the previous problem.
# Except this time print "Go to work" if it's a work day and "Sleep in" if it's
# a weekend day.

input = int(input('What day is it? Enter (0-6): '))

def conv_day(day):
    if day in range(1,6):
        print('It is a weekday. Wake up and go to work')
    else:
        print("It's the weekend! Sleep in")

conv_day(input)
