# 4. Even Numbers
# Given an list of numbers, print each number in the list that is even.


def even():
    num_list = []
    for num in range(0, 10):
        if num %2 == 0:
            num_list.append(num)
    print(num_list)

even()
