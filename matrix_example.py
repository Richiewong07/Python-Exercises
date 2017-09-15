# 8. Multiply Vectors

# Given two lists of numbers of the same length, create a new list by
# multiplying the pairs of numbers in corresponding positions in the two lists.

# Example: [2, 4, 5] x [2, 3, 6] = [4, 12, 30]

m1 = [2, 4, 5]
m2 = [2, 3, 6]


# One way to do this

answer = []

for i in range(0, len(m1)):
    answer.append(m1[i] * m2[i])

print(answer)


# Another way to do this

answer = []

for i, num1 in enumerate(m1):
    answer.append(num1 * m2[i])

print(answer)


# Same was above

answer = []

for i, num1 in enumerat(m1):
    ans = num1 * m2[i]
    answer.append(ans)

print(answer)
