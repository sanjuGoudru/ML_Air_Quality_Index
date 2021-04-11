# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 12:06:05 2021

@author: Sanjay G R
"""

from flask import Flask, render_template,url_for,request
import pandas as pd
import pickle

xgb_model = pickle.load(open('../Models/xgb_regression.pkl','rb'))

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    df = pd.read_csv('../Data/Real_Data/real_2018.csv')
    my_pred = xgb_model.predict(df.iloc[:,:-1])
    my_pred = my_pred.tolist()
    return render_template('result.html',prediction=my_pred)

if __name__ == '__main__':
    app.run(debug=True)

