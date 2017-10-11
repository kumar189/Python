# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:07:59 2017

@author: MANI
"""
#imports all the datasets and packages for the file
from sklearn import svm
from sklearn import datasets, metrics
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.svm import LinearSVC

#loads the digits data set
digitsdatasets = datasets.load_digits() 
x=digitsdatasets.data
y=digitsdatasets.target
#creates the training and test data sets with test size 0.2 which is used for cross validation
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2)  
#linear SVC function is applied
model =LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
     intercept_scaling=1, loss='squared_hinge', max_iter=1000,
     multi_class='ovr', penalty='l2', random_state=0, tol=0.0001,
     verbose=0)
# fits and predict for linear model
y_pred = model.fit(x_train, y_train).predict(x_test)
#prints the socre of model
print("For linear SVC fit",model.score(x,y))
#prints the accuracy score
print("Accuracy for Linear SVC : ", metrics.accuracy_score(y_test,y_pred))
#loads data into rbf kernel
model = svm.SVC(kernel='rbf', gamma=0.03)
#fits and predicts the data into rbf kernel
y_pred = model.fit(x_train, y_train).predict(x_test)
#prints the score and accuracy score for rbf kernel
print("For rbf Kernel fit", model.score(x,y))
print("Accuracy for rbf kernel : ",metrics.accuracy_score(y_test,y_pred))