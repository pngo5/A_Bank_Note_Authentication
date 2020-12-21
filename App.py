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

if __name__=='__main__':
    app.run()