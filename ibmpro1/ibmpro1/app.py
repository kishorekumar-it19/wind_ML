"""
Author name :Harish M, Kishore Kumar M,Deepak Raja  
Team name   :PROZONE
Project name:Wind analysis prediction using AI
"""

#mycursor = mydb.cursor()
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/login',methods=['POST'])


def predict():#calculator page
    '''
    For rendering results on HTML GUI
    '''
    ws=float(request.form['windspeed'])#Getting windspeed from user
    di=request.form['wind direction']#Getting windirection from user
    if di=="east" or "EAST" or "East":
        di=1
    elif di=="west" or "WEST" or "West":
        di=2
    elif di=="north" or "North" or "NORTH":
        di=3
    elif di=="south" or "South" or "SOUTH":
        di=4
    elif di=="northeast" or "Northeast" or "NORTHEAST":
        di=5
    elif di=="northwest"or "Northwest" or "NORTHWEST":
        di=6
    elif di=="southeast" or "SOUTHEAST" or "Southeast":
        di=7
    elif di=="southwest" or "SOUTHWEST" or "Southwest":
        di=8
    int_features=[]
    int_features.append(ws)
    int_features.append(di)
    final_features = [np.array(int_features)]#converting the input into an array
    prediction = model.predict(final_features)#calculating predicted output
    output = abs(np.around(prediction[0][0],2))#storing the value in a variable named output
    if float(output)>2.25:#Condition to check the factor that output is greater than 2.25
        result="\nThe Output power Satisfy the Company's need"
    else:
         result="\nThe Output Power Unable to Satisfy the Company's need"
    return render_template('index.html', prediction_text='The power to be generated is {} Mega Watts'.format(output),a=result) #To print the predicted output on the web page

if __name__ == "__main__":
   
    app.run(port=3055) #To run on the port 3055
