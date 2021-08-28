from numpy.lib.financial import irr
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# data
iris = load_iris()

iris_data = iris.data

iris_lable = iris.target

print(iris_lable)
print(iris.target_names)

# to df
iris_df = pd.DataFrame(data=iris_data, columns=iris.feature_names)
iris_df['lable'] = iris.target
iris_df.head(3)
