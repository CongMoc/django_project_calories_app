import numpy as np
from csv import reader
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression

theta_last = []
J_cost = []
scale = StandardScaler()
#Load csv
def load_csv(filename, columns):
    dataset = list()
    dataset = pd.read_csv(filename,skiprows = 1)
    dataset.columns=columns
    # drop data not important
    dataset = dataset.drop(columns='How important is exercise to you ?')
    dataset = dataset.drop(columns=['Do you have fitness equipment?','Prevent you from exercising more regularly?','prevents you from eating a healthy balanced diet','What form(s) of exercise do you currently participate in ?(Please select all that apply)','Do you exercise?','How healthy do you consider yourself?','Have you ever recommended your friends to follow a fitness routine?'])
    return dataset
        
#Standardization values
def data_standardization_number(dataset):
    lb = LabelEncoder()
    dataset['Gender'] = lb.fit_transform(dataset['Gender'])
    dataset['Describe your level of fitness'] = lb.fit_transform(dataset['Describe your level of fitness'])
    dataset['Time you exercise in week'] = lb.fit_transform(dataset['Time you exercise in week'])
    dataset['Time you exercise in day'] = lb.fit_transform(dataset['Time you exercise in day'])
    dataset['Long time you exercise in day'] = lb.fit_transform(dataset['Long time you exercise in day'])
    dataset['Do you eat a healthy balanced diet?'] = lb.fit_transform(dataset['Do you eat a healthy balanced diet?'])
    dataset['Health care motivation'] = lb.fit_transform(dataset['Health care motivation'])
    
#Train split data
def divide_variables_scale_data_calories(dataset):
    matrix = dataset.values
    row, columns = matrix.shape
    X_columns = matrix[:,0:columns-8]
    X_columns = scale.fit_transform(X_columns)
    X = np.insert(X_columns,0, values=1,axis=1)
    Y = matrix[:,columns-1:columns]
    return X, Y ,row

def divide_variables_scale_data_body(dataset):
    matrix = dataset.values
    row, columns = matrix.shape
    X_columns = matrix[:,0:columns-8]
    X_columns = scale.fit_transform(X_columns)
    X = np.insert(X_columns,0, values=1,axis=1)
    Y = matrix[:,columns-1:columns]
    return X, Y ,row
#data test 
def input_test():
    gender = input('Enter gender: ')
    age = float(input('Enter age: '))
    if gender == 'Male':
        gender = 1
        age = age * 6.755
    else:
        gender = 0
        age = age * 4.6756
    height = float(input('Enter height: '))
    weight = float(input('Enter weight: '))
    timeweek = input("Enter time exercise in week(2 to 3 day) : ")
    timeday = input("Enter time exercise in day(30 minutes): ")
    target = input("Enter your target(Loss weight or build body): ")
    return [[gender,height,weight]], age

#Standardization input data
def scale_data_test(X_test, scale):
    scaled = scale.transform(X_test)
    pred = np.insert(scaled[0], 0, values=1)
    return pred

#Prediction calories
def prediction_data(model, X_test):
    predict_calories = (X_test * model)
    return predict_calories.sum(axis=1)


#Model with gradient descent
def h_X(X, theta):
    return np.dot(X, theta.T)

def Cost_function(X,Y, theta, row):
    bias = np.power((h_X(X, theta)-Y),2)
    J = (1.0/(2*row))* np.sum(bias)
    return J

def gradientDescent(X,Y, theta, alpha, loop , row):
    theta_check = np.zeros(theta.shape)
    number_theta = theta.shape[1]
    J_check = np.zeros(loop)
    for i in range(loop):
        bias = h_X(X, theta) - Y
        for j in range(number_theta):
            Xij = np.reshape(X[:,j],(len(X),1))
            term = np.multiply(bias, Xij)
            theta_check[0,j] = theta_check[0,j] - ((alpha/len(X)) * np.sum(term))
        theta = theta_check
        J_check[i] = Cost_function(X,Y,theta , row)
    return theta, J_check
    
def mainCalories():
    columns = ['Gender','Height','Weight','How important is exercise to you ?','Describe your level of fitness','Time you exercise in week',
                    'Prevent you from exercising more regularly?','What form(s) of exercise do you currently participate in ?(Please select all that apply)',
                    'Do you exercise?','Time you exercise in day','Long time you exercise in day','Do you eat a healthy balanced diet?',
                    'prevents you from eating a healthy balanced diet','How healthy do you consider yourself?'
                    ,'Have you ever recommended your friends to follow a fitness routine?','Do you have fitness equipment?'
                    ,'Health care motivation','Body condition','Calories/day']
    dataset = load_csv('/Làm việc/Project_2_DataMining/calo/CaloriesMale.csv',columns=columns)
    data_standardization_number(dataset=dataset)
    X, Y , row = divide_variables_scale_data_calories(dataset)
    theta = np.zeros((1,X.shape[1]))
    alpha = 0.01
    loop = 1000
    theta_last, J_cost = gradientDescent(X,Y, theta, alpha, loop,row)
    return theta_last

def CheckTime(time_week):
    if time_week =="No exercise":
        time_week = 1
    elif time_week == "1 - 3 days per week":
        time_week = 1.375   
    elif time_week == "3 - 5 days per week":
        time_week = 1.55
    elif time_week == "6 - 7 days per week":
        time_week = 1.725
    else:
        time_week = 1.9
    return time_week

def input(Gender, Height, Weight, age, time_week):
    if Gender == "Male":
        Gender = 1
        age = age * 6.755
    else:
        Gender = 0
        age = age * 4.6756
    X_test = [[Gender,Height,Weight]]
    body = Weight*10000/(Height**2)
    time_week = CheckTime(time_week)
    if body < 18.5:
        body =  "Underweight"
    elif 18.5 <= body < 25:
        body = "Normal weight"
    elif 25 <= body < 30:
        body = "Overweight"
    elif 30 <= body < 35:
        body = "Obese Class I"
    elif 35 <= body < 40:
        body = "Obese Class II"
    else:
        body = "Obese Class III (Very severely obese)"
    theta_last = mainCalories()
    pred = scale_data_test(X_test=X_test, scale=scale)
    Calories = (prediction_data(theta_last, pred) - age)
    return body, Calories * time_week