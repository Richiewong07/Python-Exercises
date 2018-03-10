# 7. Multiply a list
# Given an list of numbers, and a single factor (also a number), create a new list consisting of each of the numbers in the first list multiplied by the factor. Print this list.


def mutiply():
    num_list = []
    for num in range (0, 10):
        num_list.append(num * 4)
    print(num_list)

mutiply()
