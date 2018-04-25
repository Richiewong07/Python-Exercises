# WORKING WITH A FILE'S CONTENT

file_name = 'text_files/pi_digits.txt'

with open(file_name) as file_objects:
    lines = file_objects.readlines()
    print(lines)

pi_string = ''  # CREATE VARIABLE TO HOLD DIGITS OF PI
for line in lines:  # CREATE LOOP TO ADD EACH LINE OF DIGITS TO pi_string & REMOVE NEWLINE CHAR FROM EACH LINE
    pi_string += line.strip()   # strip() -> REMOVES WHITESPACE ON THE LEFT

print(pi_string)    # PRINT STRING AND LENGTH OF STRING
print(len(pi_string))



# LARGE FILES: ONE MILLION DIGITS

file_name = 'text_files/million_digits_of_pi.txt'

with open(file_name) as file_objects:
    lines = file_objects.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))
