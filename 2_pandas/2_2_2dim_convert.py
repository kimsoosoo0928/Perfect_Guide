import numpy as np
import pandas as pd

# 3개의 컬럼명이 필요함 
col_name = ['col1', 'col2', 'col3']

# 2x3 형태의 리스트와 ndarray 생성한 뒤 이를 DataFrame으로 변환 

list = [[1,2,3],
        [11,12,13]]

array = np.array(list)

print('array shape', array.shape)
# array shape (2, 3) 

df_list = pd.DataFrame(list, columns=col_name)
print('2차원 리스트로 만든 DataFrame : \n', df_list)
# 2차원 리스트로 만든 DataFrame : 
#     col1  col2  col3
# 0     1     2     3
# 1    11    12    13

df_array = pd.DataFrame(array, columns=col_name)
print('2차원 ndarray로 만든 DataFrame : \n', df_array)
# 2차원 ndarray로 만든 DataFrame :
#     col1  col2  col3
# 0     1     2     3
# 1    11    12    13