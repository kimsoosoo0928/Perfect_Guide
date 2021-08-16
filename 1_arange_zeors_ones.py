import numpy as np

sequence_array = np.arange(10)
print(sequence_array)
print(sequence_array.dtype, sequence_array.shape)
# [0 1 2 3 4 5 6 7 8 9]
# int32 (10,)

zero_array = np.zeros((3,2), dtype='int32')
print(zero_array)
print(zero_array.dtype, zero_array.shape)

# [[0 0]
#  [0 0]
#  [0 0]]
# int32 (3, 2)

one_array = np.ones((3, 2))
print(one_array)
print(one_array.dtype, one_array.shape)

# [[1. 1.]
#  [1. 1.]
#  [1. 1.]]
# float64 (3, 2)
