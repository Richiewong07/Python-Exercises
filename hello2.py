# Same as the first exercise, but this time print the user's name in ALL CAPS,
# and also tell them the number of letters in their name.

name = input('What is your name?').upper()
letter = str(len(name))
print('HELLO ' + name + '!')
print('YOUR NAME HAS ' , letter , ' LETTERS IN IT! AWESOME!')
