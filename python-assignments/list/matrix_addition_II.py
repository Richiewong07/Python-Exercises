
# answer = []
#
# for i in range(0, len(a)):
#     row = []
#     for j in range(0, len(a[0])):
#         row.append(a[i][j]+ b[i][j])
#     answer.append(row)
# print(answer)


m1 = [[1, 3], [2, 4]]
m2 = [[5, 2], [1, 0]]

def matrix_add(a, b):

    for i in range(0, len(a)):
        row = []
        for j in range(0, len(a[0])):
            row.append(a[i][j] + b[i][j])
        print(row)

matrix_add(m1, m2)
