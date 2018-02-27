x = 50

def func(x):
    print(f'X is {x}')

    # Local Reassignment!
    x = 200
    print(f'I JUST LOCALLY CHANGED X TO {x}')


print(x)
func(x)
