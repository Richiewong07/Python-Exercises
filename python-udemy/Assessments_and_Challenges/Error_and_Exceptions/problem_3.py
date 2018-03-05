# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
#
# def ask():
#     pass
#
#
# ask()
#
# Input an integer: null
# An error occurred! Please try again!
# Input an integer: 2
# Thank you, your number squared is:  4


def ask():

    while True:
        try:
            n = int(input('Enter a number'))
        except:
            print('Please try again! \n')
            continue
        else:
            break

    print('Your number squared is: ')
    print(n ** 2)
