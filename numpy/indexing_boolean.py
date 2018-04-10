import numpy as np

a = np.arange(12).reshape(3,4)
print('Array a: \n', a)

# GIVES YOU BOOLEAN ARRAY > 4
b = a > 4
print('Boolean Array: \n', b)

# RETURNS ELEMENTS THAT ARE TRUE FROM PREVIOUS CASE
print('All elements greater than 4: \n', a[b])

# HOW TO REPLACE THOSE ELEMENTS (REPLACE WITH -1)
a[b] = - 1
print(a)
