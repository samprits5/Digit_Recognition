# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 12:36:54 2018

@author: sampr
"""

import numpy as np
from tkinter import *
from PIL import Image
from interface import user_interface
from sklearn import datasets, svm
from sklearn.preprocessing import MinMaxScaler
import os

def browse_file():
    tempfile = filedialog.askopenfilename(parent=root, initialdir=os.path.join(os.environ["HOMEPATH"], "Desktop"), title='Please Select A Image File',filetypes = (("JPG files","*.jpg"),("JPEG files","*.jpeg"),("PNG files","*.png"),("all files","*.*")))
    prediction(rescale_image(str(tempfile)))

def rescale_image(x):

    scaler2 = MinMaxScaler()

    img = Image.open(x).convert('L')
    
    ss = img.size
    
    if(ss[0]!=ss[1]):
        print("\nEnter a proper square image\n")
        exit()
        
    size = 8, 8
    img = img.resize(size,Image.ANTIALIAS)
    px = img.load()
    
    myLi = []
    for i in range(0,8):
        for j in range(0,8):
            myLi.append(px[j,i])
            
    myLi = np.array(myLi, dtype="float64").reshape(-1,1)
    scaler2.fit(myLi)

    scaledList = scaler2.transform(myLi).reshape(1,-1)
    
    return scaledList
    
def prediction(scaleImageData):
    
    digits = datasets.load_digits()
    scaler = MinMaxScaler()
    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))
    scaler.fit(data)
    data = scaler.transform(data)
    
    classifier = svm.SVC(gamma=0.20, C=100)
    
    classifier.fit(data, digits.target)
    res = classifier.predict([scaleImageData[0]])
    
    lbl["text"]="Predicted Value : "+str(res[0])
    
root = Tk()
root.title('Digit Image Recognition Program')

fm = user_interface(root)
fm.pack(side=TOP, expand=NO, fill=NONE)

root.mainloop()               