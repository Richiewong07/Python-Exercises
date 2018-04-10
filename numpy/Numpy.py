import numpy as np

import time
import sys

# SINGLE DIMENSIONAL ARRAY
a = np.array([1, 2, 3])
print(a)

# MULTIDIMENSIONAL array
b = np.array([(1,2,3), (4,5,6)])
print(b)

# range INTERGER VALUES UP UNTIL THAT VALUE
# GETS SPACE OCCUPY BY THE LIST --> getsizeof GETS MEMORY
list = range(1000)
print(sys.getsizeof(5) * len(list))

# GETS MEMORY OCCUPY BY np.arrange --> OCCUPIES LESS MEMORY
array = np.arange(1000)
print(array.size * array.itemsize)

# LIST TIME VS ARRANGE TIME
size = 100000
l1 = range(size)
l2 = range(size)

start = time.time()
result = [(x + y) for x,y in zip(l1, l2)]
print("pyton list took: ", (time.time() - start) * 1000)

a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()
result = a1 + a2
print("numpy took: ", (time.time() - start) * 1000)
