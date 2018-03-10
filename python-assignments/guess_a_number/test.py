import random

guess_tried = 0
secret_number = random.randint(1, 10)
print ('I am thinking of a number between 1 and 10.')
print('You have 5 guesses left.')
while True:
    guess_left = 5 - guess_tired
    print('You have {} guess left.'.format(guess_left))
    if guess_tried == 5:
        print('You ran out of guesses!')
        break
    while True:
        try:
            guess = int(input("What's the number? "))
            break
    if guess == secret_number:
        print('Yes! You win!')
        break
    elif guess > secret_number:
        print(str(guess) + ' is too high. Try again')
    elif guess < secret_number:
        print(str(guess) + ' is too low. Try again')
    else:
        print('Nope, try again.')


        # Have not finish yet
