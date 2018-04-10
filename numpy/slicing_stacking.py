import numpy as np

a = np.array([6,7,8])
print(a)

# HOW TO SLICE ARRAY
print(a[0:2])
print(a[-1])

a = np.array([[6,7,8], [1,2,3], [9,3,2]])
print(a)

# ROW 1 COLUMN 2 --> 3
print(a[1,2])

# FROM 0 TO 2ND ROW, COLUMN 2 --> [8,3]
print(a[0:2,2])

# GIVES LAST ELEMENT
print(a[-1])

# GIVES LAST ELEMENT, ELEMENTS 0 AND 1
print(a[-1, 0:2])

# : GIVES ALL THE ROWS, COLUMNS 1 AND 2
print(a[:, 1:3])

# ITERATE THROUGH ROWS
for row in a:
    print(row)

# FLATTEN LIST
for cell in a.flat:
    print(cell)
