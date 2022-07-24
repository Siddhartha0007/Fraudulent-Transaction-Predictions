# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 19:52:51 2022

@author: Siddhartha-PC
"""

from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from flask import Flask,render_template,request
from joblib import dump, load
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
infile = open('Xgb_classifer_model_intelligence.pkl','rb')
model = joblib.load(infile)
#infile.close()
#model = pickle.load(open('Xgb_classifer_model_intelligence1.pkl', 'rb'))

app = Flask(__name__)

# =============================================================================
# data = pd.read_csv('new_balanced_data.csv')
# X=data.drop(['Fraud_Id'],axis=1)
# y=data[['Fraud_Id']]
# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=111)
# 
# #Standardizing the numerical columns
# col_names=['amount','oldbalanceOrg','newbalanceOrig','oldbalanceDest','newbalanceDest']
# features_train = X_train[col_names]
# features_test = X_test[col_names]
# scaler = StandardScaler().fit(features_train.values)
# features_train = scaler.transform(features_train.values)
# features_test = scaler.transform(features_test.values)
# X_train[col_names] = features_train
# X_test[col_names] =features_test
# 
# xgb_classifer= XGBClassifier(n_estimators=200,max_depth=6,booster="gbtree",learning_rate=0.005)
# xgb_classifer.fit(X_train,y_train)
# =============================================================================



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
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
