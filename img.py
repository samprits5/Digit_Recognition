# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 12:36:54 2018

@author: sampr
"""
from tkinter import *
from interface import user_interface

def app():  
    root = Tk()
    root.title('Digit Image Recognition Program')
    root.resizable(False,False)

    fm = user_interface(root)
    fm.pack(side=TOP, expand=NO, fill=NONE)

    root.mainloop()   

if __name__ == '__main__':
    app()            