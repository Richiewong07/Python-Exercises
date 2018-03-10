# 9. Matrix Addition
# Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an list of lists:
#
# [ [2, -2],
#   [5, 3] ]
# Calculate the result of adding the two matrices. The number in each position in the resulting matrix should be the sum of the numbers in the corresponding addend matrices. Example: to add
#
# 1 3
# 2 4
# and
#
# 5 2
# 1 0
# results in
#
# 6 5
# 3 4

m1 = [[1, 3], [2, 4]]
m2 = [[5, 2], [1, 0]]

def matrix_add(a, b):

    for i in range(0, len(a)):
        row = []
        for j in range(0, len(a[0])):
            row.append(a[i][j] + b[i][j])
        print(row)

matrix_add(m1, m2)
