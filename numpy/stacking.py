import numpy as np

a = np.arange(6).reshape(3,2)
b = np.arange(6, 12).reshape(3,2)

print('Array a: \n', a)
print('Array b: \n', b)

# STACK ARRAY
print('Verticaly stack array \n', np.vstack((a,b)))
print('Horizontally stack array \n', np.hstack((a,b)))


a = np.arange(30).reshape(2,15)
print('Array a: \n', a)

# SPILT AN ARRAY
result = np.hsplit(a,3)
print('Array 1: \n', result[0])
print('Array 2: \n', result[1])
print('Array 3: \n',  result[2])

result = np.vsplit(a,2)
print('Array 1: \n', result[0])
print('Array 2: \n', result[1])
