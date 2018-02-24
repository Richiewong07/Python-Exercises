# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()

results = old_macdonald('macdonald')
print(results)


# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    wordlist = text.split()
    reverse_word_list = wordlist[::-1]
    return ' '.join(reverse_word_list)

results = master_yoda('I am home')
print(results)


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
    return((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

results = almost_there(90)
print(results)
