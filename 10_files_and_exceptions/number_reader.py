import json

filename = 'numbers.json'

with open(filename) as f_obj:
    numbers = json.load(f_obj)  # USE json.load() TO LOAD INFORMATION SOTRED IN FULE AND STORE IT IN THE VARIABLE NAMES

print(numbers)
