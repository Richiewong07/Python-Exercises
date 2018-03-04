# USAGE OF DOCSTRING
# def name_function():
#     '''
#     DOCSTRING: Information about the function
#     INPUT: no input...
#     OUTPUT: Hello..
#     '''
#     print('Hello')
#
# help(name_function)



# def say_hello(name='NAME'):
#     return ('hello '+ name)
#
# result = say_hello('Jose')
#
# print(result)


# Find out if the word "dog" is in a string?

def dog_check(mystring):
    return 'dog' in mystring.lower()

result = dog_check('Dog ran away')
print(result)
