#Linear Regression model
# Required Packages

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model


# Function to get data
def get_data(file_name):
    data = pd.read_csv(file_name)
    a = data[data.medal == 'GOLD'] #filter for only gold medal
    x_parameter = []
    y_parameter = []
    for i ,j in zip(a['year'],a['time']):
        x_parameter.append([float(i)])
        y_parameter.append(float(j))
    return x_parameter,y_parameter

# Function for Fitting data to Linear model
def linear_model_main(X_parameters, Y_parameters, predict_value):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions

x,y = get_data('data.csv')
predict_value = 2020 #Year to be predicted
result = linear_model_main(x,y,predict_value)
print ("Intercept value " , result['intercept'])
print ("coefficient" , result['coefficient'])
print ("Predicted value: ",result['predicted_value'])



# Function to show the resutls of linear fit model
def show_linear_line(X_parameters,Y_parameters):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    plt.scatter(X_parameters,Y_parameters,color='blue')
    plt.plot(X_parameters,regr.predict(X_parameters),color='red',linewidth=4)
    plt.xlabel("Years")
    plt.ylabel("Time(s)")
    plt.show()
    
show_linear_line(x,y)