import numpy as np

a = np.array([[1,2], [3,4]]) #dtype=complex
print(a)

# GIVES DIMENSIONS
print(a.ndim)

# GIVES BYTE SIZE
print(a.itemsize)

# GIVES DATA TYPE
print(a.dtype)

# GIVES SIZE
print(a.size)

# GIVES DIMENSIONS rows x columns
print(a.shape)

# MAKES ARRAY FULL OF ZEROS (rows, columns)
# np.ones
print(np.zeros( (3,4) ))

# GIVE RANGE FROM X TO Y WITH STEP
print(np.arange(1,5,2))

# GENERATES NUMBER FROM X TO Y LINEARLY SPACED BY CERTAIN NUMBER
print(np.linspace(1, 5, 10))

# RESHAPES ARRAY
a = np.array([[1,2], [3,4], [5,6]])
print(a.reshape(6,1))

# FLATTENS ARRAY TO ONE DIMENSION
print(a.ravel())

# GIVES MIN ELEMENT
print(a.min())

# GIVES MAX ELEMENT
print(a.max())

# SUMS ALL ELEMENT
print(a.sum())

# SUMS ALL ELEMENT IN COLUMNS
print(a.sum(axis = 0))

# SUMS ALL ELEMNT IN ROWS
print(a.sum(axis = 1))

# GIVES SQUARE ROOT OF EACH ELEMENT
print(np.sqrt(a))

# GIVES STANDARD DEVIATION OF EACH ELEMENT
np.std(a)



a = np.array([[1, 2], [2, 3]])
b = np.array([[3, 4], [5, 6]])

# GIVES DOT PRODUCT
print(a.dot(b))
