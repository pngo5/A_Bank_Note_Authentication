# -*- coding: utf-8 -*-
"""
Created on 12/21/2020

@Phat Ngo
"""

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
#-------------------------------------------
app =Flask(__name__)

pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)


@app.route('/')
def welcome():
     return "Welcome all"
 #Testing things out
 
 #taking all the values and adding it into the predictions
 # the classifiers is going to be doing the preductions
 
#api 1 based on values (using postman to test out API GET)
#Test pass
@app.route('/predict')
def predict_note_authentication():
   variance=request.args.get('variance')
   skewness=request.args.get('skewness')
   curtosis=request.args.get('curtosis')
   entropy=request.args.get('entropy')
   prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
   return "The predicited valyes is"+ str(prediction)
    

#api 2
#Creating a post method that will take in a csv files, and return the predictions 
@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    df_test=pd.read_csv(request.files.get("file"))
    prediction=classifier.predict(df_test)
    return "The predicted values for the csv is"+ str(prediction)

# moving on to postman to test out api on postman (POST)
# Test result from the file testfile is The predicted values for the csv is[0 0 0 0 1 1 1 1 1]  
























if __name__=='__main__':
    app.run()