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
import os

def browse_file():
    tempfile = filedialog.askopenfilename(parent=root, initialdir=os.path.join(os.environ["HOMEPATH"], "Desktop"), title='Please Select A Image File',filetypes = (("JPG files","*.jpg"),("JPEG files","*.jpeg"),("PNG files","*.png"),("all files","*.*")))
    prediction(rescale_image(str(tempfile)))

def rescale_image(x):

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
            
    z = np.array(myLi)
    
    Zmax = z.max()
    
    Zmin = z.min()
    
    if(Zmax == Zmin):
        print("\nTry with a different image!\n")
        exit()
    
    scaledList = []
    for val in myLi:
        v = (20*(val-Zmin))/(Zmax-Zmin)
        scaledList.append(v)
        
    scaledList = np.array(scaledList)
    
    return scaledList
    
def prediction(scaleImageData):
    
    digits = datasets.load_digits()
    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))
    
    classifier = svm.SVC(gamma=0.001)
    
    # We learn the digits on the first half of the digits
    classifier.fit(data[:], digits.target[:])
    res = classifier.predict([scaleImageData])
    
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