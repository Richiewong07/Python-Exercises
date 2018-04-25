 # Write a while loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number.

print("Enter 'q' at anytime to quit: ")

while True:
    try:
        x = input("Enter a number: ")
        if x == 'q':
            break
        x = int(x)

        y = input("Enter another number: ")
        if y == 'q':
            break

        y = int(y)
    except ValueError:
        print('Sorry you did not enter a number.')
    else:
        sum = x + y
        print('The sum of {} and {} is {}.'.format(x, y, sum))
