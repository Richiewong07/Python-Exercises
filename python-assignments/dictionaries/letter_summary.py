# Write a letter_histogram function that takes a word as its input, and
# returns a dictionary containing the tally of how many times each letter in
# the alphabet was used in the word.


histogram = {}

def letter_histogram(word):
    for char in word:
        letter_count = word.count(char) # .count returns number of occurances in a string
        if char not in histogram:
            histogram.update({char:letter_count})   #.update adds key value pairs to the dictionary
    print(histogram)

def main():
    word = input('Please give me a word: ')
    letter_histogram(word)

if __name__ == '__main__':
    main()
