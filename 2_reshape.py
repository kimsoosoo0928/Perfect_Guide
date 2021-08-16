import numpy as np

array1 = np.arange(10)
print('array1 : \n', array1)

array2 = array1.reshape(2,5)
print('array2 : \n', array2)

array3 = array1.reshape(5,2)
print('array3 : \n', array3)

'''
array1 : 
 [0 1 2 3 4 5 6 7 8 9]
array2 :
 [[0 1 2 3 4]
 [5 6 7 8 9]]
array3 :
 [[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]
'''

array1 = np.arange(10)
print(array1)
array2 = array1.reshape(-1,5)
print('array2 shape : ', array2.shape)
array3 = array1.reshape(5,-1)
print('array3 shape : ', array3.shape)

'''
[0 1 2 3 4 5 6 7 8 9]
array2 shape :  (2, 5)
array3 shape :  (5, 2)
'''

array1 = np.arange(8)
array3d = array1.reshape((2,2,2))
print('array3d : \n', array3d.tolist())

array5 = array1.reshape((-1,1))
print('array5 : \n', array5.tolist())
print('array5 shape : \n', array5.shape)

array6 = array1.reshape((-1,1))
print('array6 : \n', array6.tolist())
print('array6 shape : \n', array6.shape)

'''
array3d :
 [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]
array5 :
 [[0], [1], [2], [3], [4], [5], [6], [7]]
array5 shape :
 (8, 1)
array6 :
 [[0], [1], [2], [3], [4], [5], [6], [7]]
array6 shape :
 (8, 1)
'''