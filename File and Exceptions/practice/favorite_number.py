# Write a program that prompts for the user’s favorite number. Use json.dump() to store this number in a file. Write a separate program that reads in this value and prints the message, “I know your favorite number! It’s _____.”

import json

number = input("What is your favorite number: ")

filename = 'favorite_number.json'

with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)
    print("Thanks! I'll remember that.")
