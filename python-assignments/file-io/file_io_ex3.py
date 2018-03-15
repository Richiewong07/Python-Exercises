# Write a program that prompts the user to enter a file name, then
# prints the letter histogram and the word histogram of the contents of the file.

from file_io_ex3_functions import letter_histogram, word_histogram


def main ():
    file_name = input('Enter file name here: ')     # test3.txt
    file_handle = open(file_name, 'r')
    word = file_handle.read()

    letter_histogram(word)
    word_histogram(word)

if __name__ == '__main__':
    main()
