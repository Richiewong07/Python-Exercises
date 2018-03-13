# 4. Leetspeak
# Given a paragraph of text as a string, print the paragraph in leetspeak. To translate a string to leetspeak, you need to replace make the following character replacements (treat all input characters as uppercase):
#
# A => 4
# E => 3
# G => 6
# I => 1
# O => 0
# S => 5
# T => 7


paragraph = input('Enter a paragraph: ').upper()

def leetsspeak(word):
    for letter in word:
        if letter == 'A':
            return word.replace('A', '4')
        if letter == 'E':
            return word.replace('E', '3')
        if letter == 'G':
            return word.replace('G', '6')
        if letter == 'I':
            return word.replace('I', '1')
        if letter == 'O':
            return word.replace('O', '0')
        if letter == 'S':
            return word.replace('S', '5')
        if letter == 'T':
            return word.replace('T', '7')


results = leetsspeak(paragraph)

print(results)
