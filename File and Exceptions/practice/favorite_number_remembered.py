# Combine the two programs from Exercise 10-11 into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user’s favorite number and store it in a file. Run the program twice to see that it works.

import json

def get_stored_number():
    filename = "favorite_number.json"
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number

def prompt_number():
    number = input("What is your favorite number: ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
    return number



def favorite_number():
    number = get_stored_number()
    if number:
        print("I know your favorite number! It's " + number + "!")
    else:
        number = prompt_number()
        print("Thanks! I'll remember that.")


favorite_number()
