# 11. De-dup
# Given an list of numbers or strings, create a new list containing the same elements as the first list, except with any duplicate values removed. Print the list.


mylist = [0, 1, 1, 2, 3, 4, 4, 4, 5]

def duplicate(list):
    newlist = []
    for num in list:
        if num not in newlist:
            newlist.append(num)
    return newlist

result = duplicate(mylist)
print(result)
