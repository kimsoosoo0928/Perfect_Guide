import numpy as np

org_array = np.array([3,1,9,5])
sort_indices = np.argsort(org_array)
print(type(org_array))
print(type(sort_indices))
print(sort_indices)
# [1 0 3 2]

org_array = np.array([3,1,9,5])
sort_indices_desc = np.argsort(org_array)[::-1]
print(sort_indices_desc)
# [2 3 0 1]

name_array = np.array(['John','Mike', 'Sarah', 'Kate', 'Samuel'])
score_array = np.array([78, 95, 84, 98, 88])

sort_indices_asc = np.argsort(score_array)
print(sort_indices_asc)
print(name_array[sort_indices_asc])

# [0 2 4 1 3]
# ['John' 'Sarah' 'Samuel' 'Mike' 'Kate']