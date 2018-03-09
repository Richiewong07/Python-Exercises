# Prompt the user for the missing words to a Madlib sentence using the input
# function. You will make up your own Madlib sentence

name = input('What is name?')
hobby = input('What do you like to do?')
color = input('What is your favorite color?')
print("My name is {0}. I like to {1} in my free time. My favorite color is {2}."
.format(name.lower(), hobby.lower(), color.lower()))
