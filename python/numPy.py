import numpy as np
# 1D array
a = np.array([1,2,3])
print(type(a))
print(a.shape)
print(a.ndim)
print(a.dtype)
# 2D array
b = np.array([[4, 5, 6],
              [7, 8, 9]])
print(b.shape)
print(b.ndim)
print(a.dtype)
# 3D array
c = np.array([[[10, 11, 12],[13, 14, 15],[16, 17, 18]]])
print(c.shape)
print(c.ndim)
print(c.dtype)

# determine how many element in array
print("total element in a, b, c array is: ",a.size, b.size, c.size)
print("total memory in a, b, c array is: ",a.nbytes, b.nbyes, c.nbyes)