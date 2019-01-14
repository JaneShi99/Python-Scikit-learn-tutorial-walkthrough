#Reference https://elitedatascience.com/python-machine-learning-tutorial-scikit-learn
#numpy: more support for numerical computtation
#Pandas: library that supports dataframes, 
import numpy as np
import pandas as pd

#module that help us choose between models
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

#training with random forest 
from sklearn.ensemble import RandomForestRegressor

#cross validation tools
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV

#evaluation metrics
from sklearn.metrics import mean_squared_error, r2_score

#use our model for future
from sklearn.externals import joblib

#loading data from csv

dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(dataset_url)

#split data into table
data = pd.read_csv(dataset_url, sep=';')

#print data.shape returns dim
#print data.describe returns statistical facts of data

#spit data into target feature/ input features
y = data.quality
X = data.drop('quality', axis=1)

#split data into training/ test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123,stratify=y)

#standardizing
scaler = preprocessing.StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

pipeline = make_pipeline(preprocessing.StandardScaler(),
                         RandomForestRegressor(n_estimators=100))

#declare hyperparameters
hyperparameters = { 'randomforestregressor__max_features' : ['auto', 'sqrt', 'log2'], 'randomforestregressor__max_depth': [None, 5, 3, 1]}

#fittig/ tuning model

clf = GridSearchCV(pipeline, hyperparameters, cv=10)

# Fit and tune model
clf.fit(X_train, y_train)

#refit on entire training set
y_pred = clf.predict(X_test)

#evaluate the outcome
pred = clf.predict(X_test)
print r2_score(y_test, pred)
print mean_squared_error(y_test, pred)


#save the model for future
joblib.dump(clf, 'rf_regressor.pkl')
