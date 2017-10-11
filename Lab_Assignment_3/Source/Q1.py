# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:40:56 2017

@author: MANI
"""

from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
import csv
#creates a dae and prices list
date_list =[]
price_list = []

print("Welcome to Stock exchange predictor using Linear Regression\n ")
#defines a function collect_data with filename as argument to read a file
def collect_data(file):  #Function to read and save collected csv data from file 'Japan_stock.csv' to lists
    rawdata = open(file , 'r')
    #reads raw data from excel file
    data = csv.reader(rawdata)
    next(data)
    #loads date and prices lists using dataset row indexes
    for row in data:
        date_list.append(int(row[0]))
        price_list.append(float(row[1]))
#function desined to predicts the predict model
def plot_predict_model(date_list, price_list, x):  #Function to plot our model and precit the stock open price on Sep. 29th
#instance created for linear regression model  
    model = linear_model.LinearRegression()
    dates = np.reshape(date_list,(len(date_list),1))
    prices = np.reshape(price_list,(len(price_list),1))
    #fits the model dates and prices
    model.fit(dates,prices)
    #plots the dates and prices on graph with blue color
    plt.scatter(dates, prices, color='blue')  #Plot of the collected data on the coordinates
    #plots the line on graph
    plt.plot(dates, model.predict(dates), color='red', linewidth=5)  # Plot of the line (model fit) formed by Linear Regreesion
    plt.show()
    #predicts the price with x as input to model.predict
    predicted_price = model.predict(x)  #Predicting the stock open price on Sep. 29th
    coef = model.coef_[0][0]  #Coefficient(m) of the model formed (Y = m*X + c)
    intercept = model.intercept_[0]  #Intercept(c) of the model formed (Y = m*X + c)
    #predicts the price for a date
    print("Predicted price for stock open on September 28th is: ",predicted_price[0][0])
    print("The coefficient and intercept of the formed model by Linear Regression are: ", coef , intercept )

#calls the function to load data
collect_data('Dow_Jone.csv')
plot_predict_model(date_list,price_list,1)