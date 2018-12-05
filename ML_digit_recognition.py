# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 12:36:54 2018

@author: sampr
"""


from tkinter import *
from tkinter import filedialog
from tkinter import font
import numpy as np
from PIL import Image
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
    
    classifier = svm.SVC(gamma=0.20, C=10)
    
    classifier.fit(data, digits.target)
    res = classifier.predict([scaleImageData[0]])
    
    lbl["text"]="Predicted Value : "+str(res[0])
    
root = Tk()
root.title('Digit Image Recognition Program')

    
fm = Frame(root, width=600, height=400, bg="white")
fm.pack(side=TOP, expand=NO, fill=NONE)

lbl2=Label(fm,width=20,bg="white",text="Algorithm : SVM Classifier",font=("Helvetica 17 bold"))
f = font.Font(lbl2, lbl2.cget("font"))
f.configure(underline=True)
lbl2.configure(font=f)
lbl2.pack(pady=10,padx=15,ipadx=8,ipady=8)

lbl=Label(fm,width=20,bg="cyan",font=("Helvetica", 20))
lbl.pack(pady=10,padx=15,ipadx=8,ipady=8)

b1=Button(fm, text="Browse File", width=10,bg="#ffcccc", fg="black",command= lambda: browse_file())
b1.pack(side=TOP,padx=5,pady=5,ipadx=8,ipady=8)
     
    
root.mainloop()               