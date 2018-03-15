# Write a program that prompts the user to enter a file name,
# reads the contents of the file and prints it to the screen.

file_name = input("Enter a file name here")
file_handle = open(file_name , 'r')
contents = file_handle.read()
file_handle.close()

print(contents)
