# Same as the first exercise, but this time print the user's name in ALL CAPS,
# and also tell them the number of letters in their name.

name = input('What is your name? ').upper()
letters = len(name)
print('Hello, {} !\nYour name has {} letters in it! Awesome!'.format(name, letters))
