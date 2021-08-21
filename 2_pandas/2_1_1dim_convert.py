import numpy as np
import pandas as pd

col_name1 = ['col']

list1 = [1,2,3]

array1 = np.array(list1)

print('array1 shape : ', array1.shape)

# array1 shape :  (3,)

# 리스트를 이용해 DataFrame 생성

df_list1 = pd.DataFrame(list1, columns=col_name1)
print('1차원 리스트로 만든 DataFrame :\n', df_list1)
# 1차원 리스트로 만든 DataFrame :
#     col
# 0    1 
# 1    2 
# 2    3 

# 넘파이 ndarray를 이용해 DataFrame 생성
df_array1 = pd.DataFrame(array1, columns=col_name1)
print('1차원 ndarray로 만든 DataFrame:\n', df_array1)
# 1차원 ndarray로 만든 DataFrame:
#     col
# 0    1
# 1    2
# 2    3