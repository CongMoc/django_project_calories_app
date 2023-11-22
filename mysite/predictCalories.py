import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from .LinearRegresstionModel import LinearRegresstion



def ReadFile(filename):
    data = pd.read_csv(filename)
    return data

def PreProcessingCalories(data):
    lb = LabelEncoder()
    data['Gender'] = lb.fit_transform(data['Gender'])
    X = data.drop(columns='Calories/day')
    X = X.drop(columns='Index : 0 - Extremely Weak 1 - Weak 2 - Normal 3 - Overweight 4 - Obesity 5 - Extreme Obesity')
    Y = data['Calories/day']
    Z = data['Index : 0 - Extremely Weak 1 - Weak 2 - Normal 3 - Overweight 4 - Obesity 5 - Extreme Obesity']
    return X,Y,Z

def TrainTestSplit(X,Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.8, random_state=100)
    return X_train, X_test, Y_train, Y_test

def TrainDataForPredictCalories(data):
    model = LinearRegression()
    X,Y,Z = PreProcessingCalories(data)
    X_train, X_test, Y_train, Y_test = TrainTestSplit(X,Y)
    model.fit(X_train, Y_train)
    return model

def TrainDataForIndex(data):
    model = LinearRegression()
    X,Y,Z = PreProcessingCalories(data)
    X_train, X_test, Y_train, Y_test = TrainTestSplit(X,Z)
    model.fit(X_train, Y_train)
    return model
#What form(s) of exercise do you currently participate in ?(Please select all that apply),Do you exercise?,What time if the day do you prefer to exercise?,How long do you spend exercising per day ?,Would you say you eat a healthy balanced diet ?,"What prevents you from eating a healthy balanced diet, If any?(Please select all that apply)",How healthy do you consider yourself?,Have you ever recommended your friends to follow a fitness routine?,Have you ever purchased a fitness equipment?,What motivates you to exercise?(Please select all that applies )

def InputDataTest():
    gender = input('Enter your gender:')
    height = int(input('Enter your height:'))
    weight = int(input('Enter your weight:'))
    importExercise = int(input('How important is exercise to you?'))
    level = str(input("How do you describe your current level of fitness ?"))
    timeExercise = str(input("How often do you exercise?"))
    timeFree  = str(input("What barriers you from exercising more regularly?"))
    
    if gender == 'Male':
        gender = 1
    else:
        gender = 0
    return [[gender,height,weight,importExercise,level,timeExercise,timeFree]]

def AgeAndExercise(male):
    age = float(input("Enter your age:"))
    exercise = float(input("Enter activity your exercise:"))
    if male == 'Female' or male == 'female':
        age = age*6.755
    else:
        age = age*4.6756
    if exercise == 0:
        exercise =  1.2
    elif exercise >= 1 or exercise <=3:
        exercise =  1.375
    elif exercise >= 4  and exercise <= 5:
        exercise = 1.55
    elif exercise >= 6 and exercise <= 7:
        exercise = 1.725
    else:
        exercise = 1.9
    return age, exercise
 
def PredictionCalories(model,X_test,age, exercise):
    Y_predict = model.predict(X_test)
    Y_predict = (Y_predict - age)*exercise
    return Y_predict

def PredictionIndex(model,X_test):
    Y_predict = model.predict(X_test)
    return Y_predict

def Main():
    X_test = InputDataTest()
    age,exercise = AgeAndExercise(X_test[0])
    data = ReadFile('/Làm việc/Project_2_DataMining/calo/CaloriesMale.csv')
    ModelsPredictionCalories = TrainDataForPredictCalories(data)
    Y_predict_calories = PredictionCalories(ModelsPredictionCalories,X_test,age,exercise)
    ModelsPredictIndex = TrainDataForIndex(data)
    Y_predict_Index = PredictionIndex(ModelsPredictIndex,X_test)
    if Y_predict_Index>=0 and Y_predict_Index <1:
        print("You are extremely weak with calories/day:"+str(Y_predict_calories))
    elif Y_predict_Index >=1 and Y_predict_Index <2:
        print("You are weak with calories/day:" +str(Y_predict_calories))
    elif Y_predict_Index >=2 and Y_predict_Index <3:
        print("You are normal with calories/day:"+str(Y_predict_calories))
    elif Y_predict_Index >= 3 and Y_predict_Index <4:
        print("You are overweight with calories/day:"+str(Y_predict_calories))
    elif Y_predict_Index >=4 and Y_predict_Index <5:
        print("You are obesity with calories/day:"+str(Y_predict_calories))
    else:
        print("You are extreme obesity with calories/day:"+str(Y_predict_calories))
if __name__ == '__main__':
    Main()