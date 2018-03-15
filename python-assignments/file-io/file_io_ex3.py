# Write a program that prompts the user to enter a file name, then
# prints the letter histogram and the word histogram of the contents of the file.

file_name = input('Enter file name here')
file_handle = open(file_name, 'r')
contents = file_handle.read()

count_letter = {}
count_word = {}

### Need to finish
