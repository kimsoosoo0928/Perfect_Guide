import numpy as np
import pandas as pd

# key는 문자열 칼럼명으로 매핑, value는 리스트 형(또는 ndarray) 칼럼 데이터로 매핑
dict = {'col1':[1,11], 'col2':[2,22], 'col3':[3,33]}
df_dict=pd.DataFrame(dict)
print('딕셔너리로 만든 DataFrame :\n', df_dict)

# 딕셔너리로 만든 DataFrame :
#     col1  col2  col3
# 0     1     2     3
# 1    11    22    33