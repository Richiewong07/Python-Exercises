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


# histogram = {}
#
# def letter_histogram(word):
#     for char in word:
#         count = word.count(char)
#         if char not in histogram:
#             histogram.update({char:count})
#     print (histogram)
#
# def main():
#     word = input("Please give me a word. >")
#     letter_histogram(word)
#
# if __name__ == '__main__':
#     main()
