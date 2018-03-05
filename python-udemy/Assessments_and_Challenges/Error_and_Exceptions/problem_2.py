# Problem 2
# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
#
# x = 5
# y = 0
#
# z = x/y
#
#
# ---------------------------------------------------------------------------
# ZeroDivisionError                         Traceback (most recent call last)
# <ipython-input-2-6f985c4c80dd> in <module>()
#       2 y = 0
#       3
# ----> 4 z = x/y
#
# ZeroDivisionError: division by zero

try:
    x = 5
    y = 0
    z = x/y
except:
    print('Error!')
finally:
    print('All done')
