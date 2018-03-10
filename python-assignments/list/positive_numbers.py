# 5. Positive Numbers
# Given an list of numbers, print each number in the list that is greater than zero.


def positive():
    num_list = []
    for num in range(-10, 10):
        if num > 0:
            num_list.append(num)
    print(num_list)

positive()
