import pandas as pd

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