histogram = {}
histogram2 = {}

def letter_histogram(word):
    for char in word:
        letter_count = word.count(char) # .count returns number of occurances in a string
        if char not in histogram:
            histogram.update({char:letter_count})   #.update adds key value pairs to the dictionary
    print(histogram)


def word_histogram(text):
    words = text.split(' ')
    for word in words:
        count = words.count(word)
        if word not in histogram2 and word != '': # to prevent logging spaces
            histogram2.update({word:count})
    print(histogram2)
