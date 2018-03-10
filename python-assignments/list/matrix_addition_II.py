
answer = []

for i in range(0, len(a)):
    row = []
    for j in range(0, len(a[0])):
        row.append(a[i][j]+ b[i][j])
    answer.append(row)
print(answer)
