# *args allows you take in as many paraments as you want
# *args returns back a tuple

def myfunc(*args):
    # print(args)
    for item in args:
        print(item)

myfunc(40,60, 100, 1, 34)



# **kwargs (keyword arguements)
# **kwargs returns back a dictionary

def myfunc(**kwargs):
    # print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc(fruit = 'apple', veggie = 'lettuce')
