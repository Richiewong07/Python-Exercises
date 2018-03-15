# Bonus Challenge
# Given a histogram tally (one returned from either letter_histogram or word_summary), print the top 3 words or letters.

histogram = {}

def word_histogram(text):
    words = text.split(' ')
    for word in words:
        count = words.count(word)
        if word not in histogram and word != '': # to prevent logging spaces
            histogram.update({word:count})
    # print(histogram)

def counter():
    countList = []
    for key, value in histogram.items():
        string = value, key
        # print(string)     # loops through and grabs key value pairs (2, 'to') --> (2, 'be')
        countList.append(string)
        # print(countList)      # adds to array [(2, 'to'), (2, 'be')]
    # countList.sort(reverse=True)      # reverse array above
    return(countList)


def main():
    text = input("Please give me some text. ").lower()
    word_histogram(text)
    sortedList = counter()
    print("The top three words are: \n1. {}\n2. {}\n3. {}".format(sortedList[0][1], sortedList[1][1], sortedList[2][1]))

if __name__ == '__main__':
    main()
