# Write a word_histogram function that takes a paragraph of text as its input,
# and returns a dictionary containing the tally of how many times each word in
# the alphabet was used in the text


histogram = {}

def word_histogram(text):
    words = text.split(' ')
    for word in words:
        count = words.count(word)
        if word not in histogram and word != '': # to prevent logging spaces
            histogram.update({word:count})
    print(histogram)

def main():
    text = input("Please give me some text: ").lower()
    word_histogram(text)


if __name__ == '__main__':
    main()
