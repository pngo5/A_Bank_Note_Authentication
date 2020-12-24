# -*- coding: utf-8 -*-
"""
Created on 12/21/2020

@Phat Ngo
"""

from flask import Flask,request
import flasgger
from flasgger import Swagger
import pandas as pd
import numpy as np
import pickle


#-------------------------------------------
app =Flask(__name__)
Swagger(app)



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
@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
    
    """
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
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
    
    """
    df_test=pd.read_csv(request.files.get("file"))
    prediction=classifier.predict(df_test)
    return str(list(prediction))

# VERY WEIRD SWAGGER BUG. Sometimes it works, and other time its doesn't.
# moving on to postman to test out api on postman (POST)
# Test result from the file testfile is The predicted values for the csv is[0 0 0 0 1 1 1 1 1]  


def main():
      st.tiltle


if __name__=='__main__':
    app.run( app.run(host='0.0.0.0',port=8000))