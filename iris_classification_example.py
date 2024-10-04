import pandas as pd
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import numpy as np
import pdb

from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('iris.data')

data.head(5)
print(data)

train, test = train_test_split(data, test_size = 0.4, stratify = data['species'], random_state = 42)


X_train = train[['sepal_length','sepal_width','petal_length','petal_width']]
y_train = train.species
X_test = test[['sepal_length','sepal_width','petal_length','petal_width']]
y_test = test.species

######## Naive Bayes Classifier  ##########################
##model = GaussianNB()
##model.fit(X_train,y_train)
##
##predicted = model.predict(X_test)
##
##print(metrics.classification_report(y_test,predicted))
##print(metrics.confusion_matrix(y_test,predicted))

######### KNN classifier    ###############################

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train)
#KNeighborsClassifier(...)
print(neigh.predict(X_test))
print(neigh.predict_proba(X_test))

