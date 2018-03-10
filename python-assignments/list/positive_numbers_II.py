# 6. Positive Numbers II
# Given an list of numbers, create a new list which contains every number in the given list which is positive.


def positive():
    num_list = []
    for num in range(-10, 10):
        if num > 0:
            num_list.append(num)
    print(num_list)

positive()
