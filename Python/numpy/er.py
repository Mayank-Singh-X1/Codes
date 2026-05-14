import numpy as np
print(np.__version__)
# create 1d array 
# array=np.array([1,2,3,4  ,5,56,5]) 
# print(array)
# print(type(array)) /numpy.ndarray

# D2array=np.array([[1,2,3], [45,56,7], [6,3,9,]])
# print(type(D2array))
# print(D2array.ndim)
# array=np.array('a')
# print(array.ndim)

#Array slicing
# array=np.array([[1,2,3,4],
#                 [5,6,7,8],
#                 [9,10,11,12],
#                 [13,14,15,16]])
# print(array[:2, 0:2]) # Syntax start:end:skip

#broadcasting
array1=np.array([[1,2,3,4,5,6,7,8,9,10]])
array2=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(array1.shape)
print(array2.shape)
print(array1 * array2)