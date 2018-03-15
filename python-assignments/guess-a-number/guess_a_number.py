import random

def play_again():
    play_again = (input('Do you want to play? Enter (Y or N): ')).upper()

    if play_again == "Y":
        guess_number()
    else:
        print('Thank you for playing!')


def guess_number():
    secret_number = random.randint(1, 10)
    print('I am thinking of a number between 1 and 10.')

    print('You have 5 guesses left.')

    count = 4

    while True:
        guess = int(input('Guess a number between 1 and 10: '))

        if guess == secret_number:
            print('Yes! You win!')
            play_again()
            break
        elif guess > secret_number:
            print('{} is too high.'.format(guess))
            print('You have {} guesses left'.format(count))
            count -=1
        elif guess < secret_number:
            print('{} is too low.'.format(guess))
            print('You have {} guesses left'.format(count))
            count -=1


        if count < 0:
            print('You have 0 gusses left. You lose!')
            play_again()
            break


guess_number()
