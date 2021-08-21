import pandas as pd
import numpy as np

titanic_df = pd.read_csv('./titanic_train.csv')
print('titanic 변수 type : ', type(titanic_df))
print(titanic_df)

print('DataFrame 크기 ', titanic_df.shape)
# DataFrame 크기  (891, 12)

titanic_df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 891 entries, 0 to 890
# Data columns (total 12 columns):
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   PassengerId  891 non-null    int64
#  1   Survived     891 non-null    int64
#  2   Pclass       891 non-null    int64
#  3   Name         891 non-null    object
#  4   Sex          891 non-null    object
#  5   Age          714 non-null    float64
#  6   SibSp        891 non-null    int64
#  7   Parch        891 non-null    int64
#  8   Ticket       891 non-null    object
#  9   Fare         891 non-null    float64
#  10  Cabin        204 non-null    object
#  11  Embarked     889 non-null    object
# dtypes: float64(2), int64(5), object(5)
# memory usage: 83.7+ KB

print(titanic_df.describe())
#        PassengerId    Survived      Pclass         Age       SibSp       Parch        Fare
# count   891.000000  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
# mean    446.000000    0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
# std     257.353842    0.486592    0.836071   14.526497    1.102743    0.806057   49.693429
# min       1.000000    0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
# 25%     223.500000    0.000000    2.000000   20.125000    0.000000    0.000000    7.910400
# 50%     446.000000    0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
# 75%     668.500000    1.000000    3.000000   38.000000    1.000000    0.000000   31.000000
# max     891.000000    1.000000    3.000000   80.000000    8.000000    6.000000  512.329200

value_counts = titanic_df['Pclass'].value_counts()
print(value_counts)
# 3    491
# 1    216
# 2    184

titanic_pclass = titanic_df['Pclass']
print(type(titanic_pclass))
# <class 'pandas.core.series.Series'>

print(titanic_pclass.head())
# 0    3
# 1    1
# 2    3
# 3    1
# 4    3

value_counts = titanic_df['Pclass'].value_counts()
print(type(value_counts))
print(value_counts)
# <class 'pandas.core.series.Series'>
# 3    491
# 1    216
# 2    184

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

# key는 문자열 칼럼명으로 매핑, value는 리스트 형(또는 ndarray) 칼럼 데이터로 매핑
dict = {'col1':[1,11], 'col2':[2,22], 'col3':[3,33]}
df_dict=pd.DataFrame(dict)
print('딕셔너리로 만든 DataFrame :\n', df_dict)

# 딕셔너리로 만든 DataFrame :
#     col1  col2  col3
# 0     1     2     3
# 1    11    22    33

array3 = df_dict.values
print('df_dict.values 타입 : ', type(array3), 'df_dict.values shape : ', array3.shape)
# df_dict.values 타입 :  <class 'numpy.ndarray'> df_dict.values shape :  (2, 3)
print(array3)
# [[ 1  2  3]
#  [11 22 33]]

# df -> list
list3 = df_dict.values.tolist()
print('df_dict.value.tolist() 타입 : ', type(list3))
# df_dict.value.tolist() 타입 :  <class 'list'>
print(list3)
# [[1, 2, 3], [11, 22, 33]]

# df -> dict
dict3 = df_dict.to_dict('list')
# df_dict.to_dict() 타입 :  <class 'dict'>
print('\n df_dict.to_dict() 타입 : ', type(dict3))
# {'col1': [1, 11], 'col2': [2, 22], 'col3': [3, 33]}
print(dict3)

titanic_df['Age_0'] = 0
print(titanic_df.head(3))

#    PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked  Age_0
# 0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S      0
# 1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C      0
# 2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S      0

titanic_df['Age_by_10'] = titanic_df['Age']*10
titanic_df['Family_No'] = titanic_df['SibSp'] + titanic_df['Parch'] + 1
print(titanic_df.head(3))
#    PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked  Age_0  Age_by_10  Family_No
# 0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S      0      220.0          2
# 1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C      0      380.0          2
# 2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S      0      260.0          1

titanic_df['Age_by_10'] = titanic_df['Age_by_10'] + 100
print(titanic_df.head(3))

#    PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked  Age_0  Age_by_10  Family_No
# 0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S      0      320.0          2
# 1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C      0      480.0          2
# 2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S      0      360.0          1

titanic_drop_df = titanic_df.drop('Age_0', axis=1)
print(titanic_drop_df.head(3))
#    PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked  Age_by_10  Family_No
# 0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S      320.0          2
# 1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C      480.0          2
# 2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S      360.0          1


print(titanic_df.head(3))
#    PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked  Age_0  Age_by_10  Family_No
# 0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S      0      320.0          2
# 1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C      0      480.0          2
# 2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S      0      360.0          1

drop_result = titanic_df.drop(['Age_0', 'Age_by_10', 'Family_No'], axis=1, inplace=True)
print('inplace=True 로 drop 후 반환된 값 : ', drop_result)
print(titanic_df.head(3))

pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 15)
print('===============before axis 0 drop==========')
print(titanic_df.head(3))

#    PassengerId  Survived  Pclass            Name     Sex   Age  SibSp  Parch          Ticket     Fare Cabin Embarked
# 0            1         0       3  Braund, Mr....    male  22.0      1      0       A/5 21171   7.2500   NaN        S
# 1            2         1       1  Cumings, Mr...  female  38.0      1      0        PC 17599  71.2833   C85        C
# 2            3         1       3  Heikkinen, ...  female  26.0      0      0  STON/O2. 31...   7.9250   NaN        S

titanic_df.drop([0,1,2], axis=0, inplace=True)
print('=============after axis 0drop ==========')
print(titanic_df.head(3))
   PassengerId  Survived  Pclass            Name     Sex   Age  SibSp  Parch  Ticket     Fare Cabin Embarked
3            4         1       1  Futrelle, M...  female  35.0      1      0  113803  53.1000  C123        S
4            5         0       3  Allen, Mr. ...    male  35.0      0      0  373450   8.0500   NaN        S
5            6         0       3  Moran, Mr. ...    male   NaN      0      0  330877   8.4583   NaN        Q