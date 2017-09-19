# Write a word_histogram function that takes a paragraph of text as its input,
# and returns a dictionary containing the tally of how many times each word in
# the alphabet was used in the text

word = input("Enter paragraph here")

count = {}

for word in paragraph:
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1

print(count)
