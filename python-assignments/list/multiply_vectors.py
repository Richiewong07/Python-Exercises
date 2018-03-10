# 8. Multiply Vectors
# Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists. Example:
#
# [2, 4, 5] x [2, 3, 6] = [4, 12, 30]


a = [2, 4, 5]
b = [2, 3, 6]

def vectors(m1, m2):
    num_list = []
    for num in range(0, len(m1)):
        num_list.append(m1[num] * m2[num])
    print(num_list)

vectors(a, b)
