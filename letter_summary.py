# Write a letter_histogram function that takes a word as its input, and
# returns a dictionary containing the tally of how many times each letter in
# the alphabet was used in the word.

word = input("Enter word summary here")

count = {}

for n in word:
    if n not in count:
        count[n] = 1
    else:
        count [n] += 1

print(count)
