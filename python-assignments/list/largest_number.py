
# 2. Largest Number
# Given an list of numbers, print the largest of the numbers.

num_list = [0, 5, 10, 18, -1, 5]

def largest(numbers):
    numbers.sort()
    return numbers[-1]

print(largest(num_list))
