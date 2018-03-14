# 1. 1 to 10
# Using a for loop and the range function, print out the numbers between 1 and 10 inclusive, one on a line. Example output:
#
# $ python 1_to_10.py
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

def counter(count):
    while count in range(0,10):
        count += 1
        print(count)

counter(0)
