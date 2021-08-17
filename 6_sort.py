import numpy as np

org_array = np.array([3,1,9,5])
sort_array1 = np.sort(org_array)
print(sort_array1) # [1 3 5 9]
print(org_array)
sort_array2 = org_array.sort()
print(sort_array2)
print(org_array)

# [1 3 5 9]
# [3 1 9 5]
# None
# [1 3 5 9]

sort_array1_desc = np.sort(org_array)[::-1]
print(sort_array1_desc)
# [9 5 3 1]

array2d = np.array([[8,12],[7,1]])
sort_array2d_axis0 = np.sort(array2d, axis=0)
print(sort_array2d_axis0)

# [[ 7  1]
#  [ 8 12]]

sort_array2d_axis1 = np.sort(array2d, axis=1)
print(sort_array2d_axis1)

# [[ 8 12]
#  [ 1  7]]