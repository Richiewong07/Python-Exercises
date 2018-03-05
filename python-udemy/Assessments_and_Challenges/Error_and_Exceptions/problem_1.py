# Problem 1
# Handle the exception thrown by the code below by using try and except blocks.
#
# for i in ['a', 'b' 'c']:
#     print(i ** 2)
#
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-1-c35f41ad7311> in <module>()
#       1 for i in ['a','b','c']:
# ----> 2     print(i**2)
#
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

try:
    for i in ['a', 'b', 'c']:
        print (i ** 2)
except:
    print('General Error!' Watch out!)
