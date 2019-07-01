from tkinter import *
from tkinter import filedialog
from tkinter import font


class user_interface(Frame):
	"""docstring for user_interface"""
	def __init__(self, root):

		self.parent = root

		super().__init__(root, width=600, bg="white")
		
		lbl2=Label(root,width=40,bg="white",text="Algorithm : SVM Classifier",font=("Helvetica 17 bold"))
		f = font.Font(lbl2, lbl2.cget("font"))
		f.configure(underline=True)
		lbl2.configure(font=f)
		lbl2.pack(pady=10,padx=15,ipadx=8,ipady=8)

		lbl=Label(root,width=40,bg="cyan",font=("Helvetica", 17))
		lbl.pack(pady=10,padx=15,ipadx=8,ipady=8)

		b1=Button(root, text="Browse File", width=10,bg="#ffcccc", fg="black",command= lambda: browse_file())
		b1.pack(side=TOP,padx=5,pady=5,ipadx=8,ipady=8)


