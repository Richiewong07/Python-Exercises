# Exercise​ ​2:

# Write​ ​a​ ​function​ ​that​ ​find​ ​the​ ​frequency​ ​occurrence​ ​of​ ​a​ ​letter​ ​in​ ​a​ ​sentence.​ ​The​ ​function​ ​should return​ ​an​ ​integer.​ ​(Do​ ​not​ ​use​ ​the​ ​​str​.count()​ ​default​ ​python​ ​function)

# Examples:
# find_frequency(“t”,​ ​“this​ ​is​ ​a​ ​test”)​ ​→​ ​3
# find_frequency(“y”,​ ​“this​ ​is​ ​a​ ​test”)​ ​→​ ​0


def find_frequency(letter, sentence):
    """Function loops through the inputed string and counts the number of occurrences of the search letter."""

    letter_count = 0
    for char in sentence.lower():
        if char == letter:
            letter_count += 1
    print(letter_count)


find_frequency("t", "this is a test")
find_frequency("y", "this is a test")
