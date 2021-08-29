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

# [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
#  0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
#  2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
#  2 2]
# ['setosa' 'versicolor' 'virginica']

iris_df = pd.DataFrame(data=iris_data, )

x_train, x_test, y_train, y_test = train_test_split(iris_data, iris_lable, test_size=0.2, random_state=11)

df_clf = DecisionTreeClassifier(random_state=11)

df_clf.fit(x_train, y_train)

pred = df_clf.predict(x_test)

from sklearn.metrics import accuracy_score

print('acc : {0:.4f}'.format(accuracy_score(y_test, pred)))