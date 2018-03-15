# Write a program that prompts the user to enter a file name, then prompts the
# user to enter the contents of the file, and then saves the content to the file.

file_name = input('Enter file name here')
file_contents = input('Enter file contents here')

file_handle = open(file_name , 'w')
file_handle.write('Some text')
file_handle.close
