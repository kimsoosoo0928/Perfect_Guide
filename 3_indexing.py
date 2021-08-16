import numpy as np
array1 = np.arange(start=1, stop=10)
print('array1 : ', array1)

value = array1[2]
print('value : ', value)
print(type(value))

'''
array1 :  [1 2 3 4 5 6 7 8 9]
value :  3
<class 'numpy.int32'>
'''

array1d = np.arange(start=1, stop=10)
array2d = array1d.reshape(3, 3)
print(array2d)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print('(row=0, col=0) index 가리키는 값 : ', array2d[0, 0])
print('(row=1, col=0) index 가리키는 값 : ', array2d[1, 0])
print('(row=0, col=1) index 가리키는 값 : ', array2d[0, 1])
print('(row=2, col=2) index 가리키는 값 : ', array2d[2, 2])
