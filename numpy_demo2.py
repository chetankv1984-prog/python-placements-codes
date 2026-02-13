import numpy as np

# create 3x4 array
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# slicing first 2 rows and columns 1 and 2
b = a[:2, 1:3]

print(a[0, 1])   # before change

b[0, 0] = 77     # change in slice

print(a[0, 1])   # after change
