
# Guess Game 2
# In a previous exercise, we've written a program that "knows" a number and asks a user to guess it.
#
# This time, we're going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
#
# At the end of this exchange, your program should print out how many guesses it took to get your number.
#
# As the writer of this program, you will have to choose how your program will strategically guess. A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. But that's not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed. After you've written the program, try to find the optimal strategy!

def computer_guess(num):
    low = 1
    high = 100
    guess = 50
    while guess != num:
        guess = (low+high)//2
        print("The computer takes a guess...", guess)
        if guess > num:
            high = guess
        elif guess < num:
            low = guess + 1

    print("The computer guessed", guess, "and it was correct!")


def main():
    num = int(input("Enter a number: "))
    if num < 1 or num > 100:
        print("Must be in range [1, 100]")
    else:
        computer_guess(num)

if __name__ == '__main__':
    main()
