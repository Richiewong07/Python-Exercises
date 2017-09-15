def yes_or_no(question):
    while True:
        reply = input('Do you want to play again (Y/N)')
        if reply == 'Y':
            return True
        elif reply == 'N':
            return False
        else:
            print ("Respond with Y or No")
