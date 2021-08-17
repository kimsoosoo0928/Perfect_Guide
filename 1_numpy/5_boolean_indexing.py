import numpy as np
array1d = np.arange(start=1, stop=10)
array3 = array1d[array1d > 5]
print('array1d > 5 불린 인덱싱 결과 값 :', array3)

# array1d > 5 불린 인덱싱 결과 값 : [6 7 8 9]

print(array1d > 5)

# [False False False False False  True  True  True  True]

boolean_indexes = np.array([False, False, False, False, False,  True,  True,  True,  True])
array3 = array1d[boolean_indexes]
print("불린 인덱스로 필터링 결과 : ", array3)

# 불린 인덱스로 필터링 결과 :  [6 7 8 9]

indexes = np.array([5,6,7,8])
array4 = array1d[indexes]
print('일반 인덱스로 필터링 결과', array4)
# 일반 인덱스로 필터링 결과 [6 7 8 9]
