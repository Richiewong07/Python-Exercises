# Write a program that prompts the user to enter a file name,
# reads the contents of the file and prints it to the screen.

def main():
    file_name = input("Enter a file name here: ")   # test2.txt
    file_handle = open(file_name , 'r')
    contents = file_handle.read()
    file_handle.close()

    print(contents)

if __name__ == '__main__':
    main()
