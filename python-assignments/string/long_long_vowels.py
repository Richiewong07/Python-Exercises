# 5. Long-long Vowels
# Given a word as a string, print the result of extending any long vowels to the length of 5. Examples:
#
# Good => Goooood
# Cheese => Cheeeeese
# Man => Man
# Spoon => Spooooon

string = input('Enter Word: ')

def long_vowels(word):
    long = ['aa', 'ee', 'ii', 'oo', 'uu']
    result = ''
    for i in range(len(word)):
        two_letters = word[i:i+2]
        if two_letters in long:
            result += word[i] * 4
        else:
            result += word[i]
    return result

results = long_vowels(string)
print(results)
