import random

def play_again():
    play_again = input("Do you want to play again (Y or N)?").upper()
    if play_again == "Y":
        guess_number()
    else:
        print("Good Bye!")
        

def guess_number():
    secret_number = random.randint(1,10)
    print("I am thinking of a number between 1 and 10.")
    print("You have 5 guesses left.")
    count = 4

    while count >= 0:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == secret_number:
            print("Yes! You win!")
            play_again()
            break

        elif count == 0:
            print("You ran out of guesses!")
            play_again()
            break

        elif guess > secret_number:
            print("{} is too high. Try again".format(guess))
            print("You have {} guesses left".format(count))

        else:
            print("{} is too low. Try again".format(guess))
            print("You have {} gussess left.".format(count))

        count -= 1

play_again()
guess_number()
