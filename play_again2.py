def play_again():
    while True:
        reply = input("Do you want to play again (Y or N)?").upper()
        if reply == "Y":
            print("True")
        elif reply == "N":
            print("False")
        elif reply != "Y" or reply != "N":
            print("Invalid input")
        break

play_again()
