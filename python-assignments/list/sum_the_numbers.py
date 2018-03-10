
# 1. Sum the Numbers
# Given an list of numbers, print their sum. When I say given something, just make something up and store it in a variable.


num_list = [1, 2, 3, 4, 5]

def sum(numbers):

    total = 0

    for num in numbers:
        total += num
    print(total)


sum(num_list)
