# Write a letter_histogram function that takes a word as its input, and
# returns a dictionary containing the tally of how many times each letter in
# the alphabet was used in the word.

word = input("Enter word summary here")
word_list  = word.spilt()

count = {}

for n in word_list:
    if n not in word_list:
        count[n] = 1
    else:
        count[n] += 1

print(count)
