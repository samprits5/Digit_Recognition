# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 12:36:54 2018

@author: sampr
"""
from tkinter import *
from interface import user_interface as UI

def app():  
    root = Tk()
    root.title('Digit Image Recognition Program')
    root.resizable(False,False)
    root.geometry('700x500+350+50') 

    fm = UI(root)
    fm.place(x=0, y=0)

    root.mainloop()   

if __name__ == '__main__':
    app()            