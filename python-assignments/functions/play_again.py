# 8. Play again?
# Write a function that prompts the user for input, asking them "Do you want to play again (Y on N)?". If the user answers "Y", the function should return True, otherwise, it should return False.


def yes_or_no():
    while True:
        reply = input('Do you want to play again (Y/N)')
        if reply == 'Y':
            print ('True')
        elif reply == 'N':
            print ('False')
            breakc

yes_or_no()
