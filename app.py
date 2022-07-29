# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 19:52:51 2022

@author: Siddhartha-PC
"""

from flask import Flask, render_template, request
import pickle
import numpy as np
from flask import Flask,render_template,request
from joblib import dump, load
from jinja2 import escape
import joblib
from xgboost import XGBClassifier
infile = open('Xgb_classifer_model_intelligence.pkl','rb')
model = joblib.load(infile)
#infile.close()
#model = pickle.load(open('Xgb_classifer_model_intelligence1.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST','GET'])
def home():
    data1 = request.form['amount']
    data2 = request.form['oldbalanceOrg']
    data3 = request.form['newbalanceOrig']
    data4 = request.form['oldbalanceDest']
    data5 = request.form['newbalanceDest']
    data6 = request.form['typeId']
    arr = np.array([data1, data2, data3, data4, data5, data6],dtype=object).reshape(1,-1)
    pred = model.predict(arr)
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)
