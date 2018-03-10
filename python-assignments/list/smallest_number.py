
# 3. Smallest Number
# Given an list of numbers, print the smallest of the numbers.

num_list = [9, -2, 5, 3, 1]

def smallest(numbers):
    numbers.sort()
    return numbers[0]

print(smallest(num_list))
