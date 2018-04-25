import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'   # CHOOSE FILE NAME TO STORE THE LIST
with open(filename, 'w') as f_obj:    # OPEN FILE TOWRITE DATA TO FILE
    json.dump(numbers, f_obj)   # TO STORE LIST NUMBERS TO FILE
