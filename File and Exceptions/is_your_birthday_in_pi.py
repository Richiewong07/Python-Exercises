# IS YOUR BIRTHDAY CONTAINED IN PI?

file_name = 'text_files/million_digits_of_pi.txt'

with open(file_name) as file_objects:
    lines = file_objects.readlines()


pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form (mmddyy): ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
