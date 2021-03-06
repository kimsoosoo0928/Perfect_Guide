import pandas as pd
import numpy as np
from pandas.core import groupby, series

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
#    PassengerId  Survived  Pclass            Name     Sex   Age  SibSp  Parch  Ticket     Fare Cabin Embarked
# 3            4         1       1  Futrelle, M...  female  35.0      1      0  113803  53.1000  C123        S
# 4            5         0       3  Allen, Mr. ...    male  35.0      0      0  373450   8.0500   NaN        S
# 5            6         0       3  Moran, Mr. ...    male   NaN      0      0  330877   8.4583   NaN        Q

# 원본 파일 다시 로딩
titanic_df = pd.read_csv('./titanic_train.csv')
# index 객체 추출
indexes = titanic_df.index
print(indexes)
# RangeIndex(start=0, stop=891, step=1) 

# index 객체를 실제 값 array로 변환
print('index 객체 array값 : \n', indexes.values)
# index 객체 array값 :
#  [  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17
#   18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35
#   36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53
#   54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71
#   72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89
#   90  91  92  93  94  95  96  97  98  99 100 101 102 103 104 105 106 107
#  108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125
#  126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143
#  144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161
#  162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179
#  180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197
#  198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215
#  216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233
#  234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251
#  252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269
#  270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287
#  288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305
#  306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323
#  324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341
#  342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359
#  360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377
#  378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 394 395
#  396 397 398 399 400 401 402 403 404 405 406 407 408 409 410 411 412 413
#  414 415 416 417 418 419 420 421 422 423 424 425 426 427 428 429 430 431
#  432 433 434 435 436 437 438 439 440 441 442 443 444 445 446 447 448 449
#  450 451 452 453 454 455 456 457 458 459 460 461 462 463 464 465 466 467
#  468 469 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485
#  486 487 488 489 490 491 492 493 494 495 496 497 498 499 500 501 502 503
#  504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521
#  522 523 524 525 526 527 528 529 530 531 532 533 534 535 536 537 538 539
#  540 541 542 543 544 545 546 547 548 549 550 551 552 553 554 555 556 557
#  558 559 560 561 562 563 564 565 566 567 568 569 570 571 572 573 574 575
#  576 577 578 579 580 581 582 583 584 585 586 587 588 589 590 591 592 593
#  594 595 596 597 598 599 600 601 602 603 604 605 606 607 608 609 610 611
#  612 613 614 615 616 617 618 619 620 621 622 623 624 625 626 627 628 629
#  630 631 632 633 634 635 636 637 638 639 640 641 642 643 644 645 646 647
#  648 649 650 651 652 653 654 655 656 657 658 659 660 661 662 663 664 665
#  666 667 668 669 670 671 672 673 674 675 676 677 678 679 680 681 682 683
#  684 685 686 687 688 689 690 691 692 693 694 695 696 697 698 699 700 701
#  702 703 704 705 706 707 708 709 710 711 712 713 714 715 716 717 718 719
#  720 721 722 723 724 725 726 727 728 729 730 731 732 733 734 735 736 737
#  738 739 740 741 742 743 744 745 746 747 748 749 750 751 752 753 754 755
#  756 757 758 759 760 761 762 763 764 765 766 767 768 769 770 771 772 773
#  774 775 776 777 778 779 780 781 782 783 784 785 786 787 788 789 790 791
#  792 793 794 795 796 797 798 799 800 801 802 803 804 805 806 807 808 809
#  810 811 812 813 814 815 816 817 818 819 820 821 822 823 824 825 826 827
#  828 829 830 831 832 833 834 835 836 837 838 839 840 841 842 843 844 845
#  846 847 848 849 850 851 852 853 854 855 856 857 858 859 860 861 862 863
#  864 865 866 867 868 869 870 871 872 873 874 875 876 877 878 879 880 881
#  882 883 884 885 886 887 888 889 890]

print(type(indexes.values))
print(indexes.values.shape)
print(indexes[:5].values)
print(indexes.values[:5])
print(indexes[6])

# <class 'numpy.ndarray'>
# (891,)
# [0 1 2 3 4]
# [0 1 2 3 4]
# 6

# indexes[0] = 5
# TypeError("Index does not support mutable operations")

series_fair = titanic_df['Fare']
print('Fair Series max 값 : ', series_fair.max())
print('Fair Series sum 값 : ', series_fair.sum())
print('sum() Fair Series : ', sum(series_fair))
print('Fair Series + 3 :\n', (series_fair + 3).head(3))

#  0    10.2500
# 1    74.2833
# 2    10.9250
# Name: Fare, dtype: float64

titanic_reset_df = titanic_df.reset_index(inplace=False)
print(titanic_reset_df.head(3))
#    index  PassengerId  Survived  Pclass            Name     Sex   Age  SibSp  Parch          Ticket     Fare Cabin Embarked
# 0      0            1         0       3  Braund, Mr....    male  22.0      1      0       A/5 21171   7.2500   NaN        S
# 1      1            2         1       1  Cumings, Mr...  female  38.0      1      0        PC 17599  71.2833   C85        C
# 2      2            3         1       3  Heikkinen, ...  female  26.0      0      0  STON/O2. 31...   7.9250   NaN        S

print('===before reset_index===')
value_counts = titanic_df['Pclass'].value_counts()
print(value_counts)
print('value_counts 객체 변수 타입 : ',type(value_counts))

# 3    491
# 1    216
# 2    184
# Name: Pclass, dtype: int64
# value_counts 객체 변수 타입 :  <class 'pandas.core.series.Series'>

new_value_counts = value_counts.reset_index(inplace=False)
print('===after reset_index===')
print(new_value_counts)
print('new_value_counts 객체 변수 타입 : ',type(new_value_counts))
#    index  Pclass
# 0      3     491
# 1      1     216
# 2      2     184
# new_value_counts 객체 변수 타입 :  <class 'pandas.core.frame.DataFrame'>

print('단일 칼럼 데이터 추출:\n', titanic_df['Pclass'].head(3))
print('\n여러 칼럼의 데이터 추출:\n', titanic_df[['Survived', 'Pclass']].head(3))
# print('[] 안에 숫자 index는 KetError 오류 발생:\n', titanic_df[0])
# 단일 칼럼 데이터 추출:
#  0    3
# 1    1
# 2    3
# Name: Pclass, dtype: int64

# 여러 칼럼의 데이터 추출:
#     Survived  Pclass
# 0         0       3
# 1         1       1
# 2         1       3

# Traceback (most recent call last):
#   File "d:\Perfect_Guide\2_pandas\titanic.py", line 333, in <module>
#     print('[] 안에 숫자 index는 KetError 오류 발생:\n', titanic_df[0])
#   File "C:\ProgramData\Anaconda3\lib\site-packages\pandas\core\frame.py", line 3024, in __getitem__
#     indexer = self.columns.get_loc(key)
#   File "C:\ProgramData\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 3082, in get_loc
#     raise KeyError(key) from err
# KeyError: 0

print(titanic_df[0:2])
#    PassengerId  Survived  Pclass            Name     Sex   Age  SibSp  Parch     Ticket     Fare Cabin Embarked
# 0            1         0       3  Braund, Mr....    male  22.0      1      0  A/5 21171   7.2500   NaN        S
# 1            2         1       1  Cumings, Mr...  female  38.0      1      0   PC 17599  71.2833   C85        C

print(titanic_df[titanic_df['Pclass'] == 3].head(3))
#    PassengerId  Survived  Pclass            Name     Sex   Age  SibSp  Parch          Ticket   Fare Cabin Embarked
# 0            1         0       3  Braund, Mr....    male  22.0      1      0       A/5 21171  7.250   NaN        S
# 2            3         1       3  Heikkinen, ...  female  26.0      0      0  STON/O2. 31...  7.925   NaN        S
# 4            5         0       3  Allen, Mr. ...    male  35.0      0      0          373450  8.050   NaN        S

# print('칼럼 위치 기반 인덱싱 데이터 추출 : ', titanic_df.ix[0, 2])
# print('칼럼 명 기반 인덱싱 데이터 추출 : ', titanic_df.ix[0, 'Pclass'])

data = {'Name' : ['Chulmin', 'Eunkyung', 'Jinwoong', 'Soobeom'],
        'Year' : [2011, 2016, 2015, 2015],
        'Gender' : ['Male', 'Female', 'Male', 'Male']
        }
data_df = pd.DataFrame(data, index=['one', 'two', 'three', 'four'])
print(data_df)
#            Name  Year  Gender
# one     Chulmin  2011    Male
# two    Eunkyung  2016  Female
# three  Jinwoong  2015    Male
# four    Soobeom  2015    Male

# data_df 를 reset_index()로 새로운 숫자형 인덱스를 생성
data_df_reset = data_df.reset_index()
data_df_reset = data_df_reset.rename(columns={'index':'old_index'})

# 인덱스값에 1을 더해서 1부터 시작하는 새로운 인덱스값 생성
data_df_reset.index = data_df_reset.index+1
print(data_df_reset)

#   old_index      Name  Year  Gender
# 1       one   Chulmin  2011    Male
# 2       two  Eunkyung  2016  Female
# 3     three  Jinwoong  2015    Male
# 4      four   Soobeom  2015    Male

print(data_df.iloc[0,0])
# Chulmin

# 오류 
# data_df.iloc[0,'Name']

# 오류
# data_df.iloc['one', 0]

print(data_df_reset.iloc[0,1])
# Chulmin

print(data_df.loc['one','Name'])
# Chulmin

print(data_df_reset.loc[1,'Name'])
# Chulmin

# 오류
# print(data_df_reset.loc[0,'Name'])

print('위치기반 iloc slicing\n', data_df.iloc[0:1, 0], '\n')

print('명령 기반 loc slicing\n', data_df.loc['one':'two','Name'])

# 위치기반 iloc slicing
#  one    Chulmin
# Name: Name, dtype: object

# 명령 기반 loc slicing
#  one     Chulmin
# two    Eunkyung
# Name: Name, dtype: object

print(data_df_reset.loc[1:2, 'Name'])
# 1     Chulmin
# 2    Eunkyung

# 불린 인덱싱 

titanic_df = pd.read_csv('titanic_train.csv')
titanic_boolean = titanic_df[titanic_df['Age']>60]
print(type(titanic_boolean))
print(titanic_boolean)


print(titanic_df[titanic_df['Age']>60][['Name','Age']].head(3))


print(titanic_df.loc[titanic_df['Age']>60,['Name','Age']].head(3))

print(titanic_df[ (titanic_df['Age']>60) & (titanic_df['Pclass']==1) & (titanic_df['Sex']=='female')])

cond1 = titanic_df['Age']>60
cond2 = titanic_df['Pclass']==1
cond3 = titanic_df['Sex']=='female'
print(titanic_df[cond1 & cond2 & cond3])

# 정렬, Aggregation 함수, GroupBy 적용


titanic_sorted = titanic_df.sort_values('Name')
print(titanic_sorted.head(3))

titanic_sorted = titanic_df.sort_values(by=['Pclass', 'Name'], ascending=False)
print(titanic_sorted.head(3))

print(titanic_df.count())

# PassengerId    891
# Survived       891
# Pclass         891
# Name           891
# Sex            891
# Age            714
# SibSp          891
# Parch          891
# Ticket         891
# Fare           891
# Cabin          204
# Embarked       889

titanic_df[['Age', 'Fare']].mean()

titanic_groupby = titanic_df.groupby(by='Pclass')
print(type(titanic_groupby))

# <class 'pandas.core.groupby.generic.DataFrameGroupBy'>

titanic_groupby = titanic_df.groupby(by='Pclass').count()
print(titanic_groupby)


titanic_groupby = titanic_df.groupby('Pclass')[['PassengerId', 'Survived']].count()
print(titanic_groupby)

#         PassengerId  Survived
# Pclass
# 1               216       216
# 2               184       184
# 3               491       491

print(titanic_df.groupby('Pclass')['Age'].agg([max, min]))

#          max   min
# Pclass
# 1       80.0  0.92
# 2       70.0  0.67
# 3       74.0  0.42

agg_format={'Age':'max', 'SibSp':'sum', 'Fare':'mean'}
print(titanic_df.groupby('Pclass').agg(agg_format))

#          Age  SibSp       Fare
# Pclass
# 1       80.0     90  84.154687
# 2       70.0     74  20.662183
# 3       74.0    302  13.675550

# 결손 데이터 처리하기
print(titanic_df.isna().head(3))

print(titanic_df.isna().sum())

# PassengerId      0
# Survived         0
# Pclass           0
# Name             0
# Sex              0
# Age            177
# SibSp            0
# Parch            0
# Ticket           0
# Fare             0
# Cabin          687
# Embarked         2

titanic_df['Cabin'] = titanic_df['Cabin'].fillna('C000')
titanic_df['Age'] = titanic_df.fillna(titanic_df['Age'].mean())
titanic_df['Embarked'] = titanic_df.fillna(titanic_df['Embarked'].fillna('S'))
print(titanic_df.isna().sum())

# PassengerId    0
# Survived       0
# Pclass         0
# Name           0
# Sex            0
# Age            0
# SibSp          0
# Parch          0
# Ticket         0
# Fare           0
# Cabin          0
# Embarked       0

def get_square(a):
        return a**2

print('3의 제곱은 : ', get_square(3))

lambda_square = lambda x : x ** 2
print("3의 제곱은 : ", lambda_square(3))

a = [1,2,3]
squares = map(lambda x : x**2, a)

titanic_df['Name_len'] = titanic_df['Name'].apply(lambda x : len(x))
print(titanic_df[['Name', 'Name_len']].head(3))

titanic_df['Child_Adult'] = titanic_df['Age'].apply(lambda x : 'Child' if x <= 15 else 'Adult')
print(titanic_df[['Age', 'Child_Adult']].head(8))

titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x : 'Child' if x <= 15 else ('Adult' if x <=60 else 'Elderly'))

print(titanic_df['Age_cat'].value_counts())

# Elderly    831
# Adult       45
# Child       15

def get_category(age):
        cat=''
        if age <=5: cat='Baby'
        elif age <=12: cat='Child'
        elif age <=18: cat='Teenager'
        elif age <=25: cat='Student'
        elif age <=35: cat='Young Adult'
        elif age <=60: cat='Adult'
        else : cat = 'Elderly'

        return cat

titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x : get_category(x))
print(titanic_df[['Age', 'Age_cat']].head())
