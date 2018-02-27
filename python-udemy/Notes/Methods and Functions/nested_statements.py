x = 50

def func(x):
    print(f'X is {x}')

    # Local Reassignment!
    x = 200
    print(f'I JUST LOCALLY CHANGED X TO {x}')


print(x)
func(x)


print(".....")


x = 50

def func(x):
    print(f'X is {x}')

    # Local Reassignment on a global variable!
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED X TO {x}')
    return x

x = func(x)
print(x)
