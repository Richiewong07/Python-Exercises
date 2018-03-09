# Prompt the user for a day of the week just like the previous problem.
# Except this time print "Go to work" if it's a work day and "Sleep in" if it's
# a weekend day.

day = int(input('Day (0-6)'))
if (day == 0 or day == 6):
    print ('Sleep in')
elif (day > 0 and day < 6):
    print ('Go to work')
