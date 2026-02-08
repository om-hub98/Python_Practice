 ## Numpy is a powerful library in Python used for numerical computing. 
 # It provides support for arrays, matrices, and many mathematical functions 
 # to operate on these data structures efficiently.

import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3])
print("1D Array :", array_1d)

matrix_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("3D Array :\n", matrix_3x3)

#vector = np.array([100, 200, 300],[1000,2000,3000],[10000,20000,30000])
# array_addition = matrix_3x3 + vector
# print("Array Addition :")
# print(array_addition)

print("Sum : ",np.sum(matrix_3x3))
print("Mean : ",np.mean(matrix_3x3))
print("Max : ",np.max(matrix_3x3))
print("Min : ",np.min(matrix_3x3))
print("Standard Deviation : ",np.std(matrix_3x3))


