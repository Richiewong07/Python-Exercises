# READING ENTIRE FILES
with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)


# FILE PATH
with open('text_files/file_name.txt') as file_object:
    contents = file_object.read()
    print(contents)


# ABSOLUTE FILE PATH
file_path = '/Users/richiewong/Documents/Python-Exercises/10_files_and_exceptions/text_files/absolute_file_path.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)


# READING LINE BY LINE
file_name = 'text_files/pi_digits.txt'      # STORE NAME OF FILE
with open(file_name) as file_objects:       # OPEN/CLOSE FILE PROPERLY
    for line in file_objects:               # LOOP THROUGH EACH LINE IN FILE OBJECT
        print(line.rstrip())


# MAKING A LIST OF LINES FROM A FILE
file_name = 'text_files/pi_digits.txt'
with open(file_name) as file_objects:
    lines = file_objects.readlines()        # ALLOWS ACCESS TO FILE OBJECT OUTSIDE OF BLOCK, readlines() --> stores lines in a list

for line in lines:                          # FOR LOOP TO PRINT EACH LINE
    print(line.rstrip())
