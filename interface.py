from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
from PIL import ImageTk, Image
from machine_learning import SVMClassifier
from threading import Thread
import os
import re
import time


class user_interface(Frame):
	"""docstring for user_interface"""
	def __init__(self, root):

		self._tempfile = ""

		self.__C = 10000

		self.__gamma = 0.22

		self.__trained = 0

		self.parent = root

		super().__init__(root, width=600, bg="white")
		
		self.algo_text=Label(root,width=60,bg="cyan",text="Algorithm : SVM Classifier",font=("Courier 20 bold"))
		f = font.Font(self.algo_text, self.algo_text.cget("font"))
		f.configure(underline=True)
		self.algo_text.configure(font=f)
		self.algo_text.place(x=-135, y=5, height=80)

		self.train_text=Label(root,text="Model will be trained on Popular MNIST Handwritten Digit Datasets.",font=("Times", 17))
		self.train_text.place(x=28,y=100)

		self.img = ImageTk.PhotoImage(Image.open("assets\\digit.png"))
		self.panel = Label(root, image = self.img)
		self.panel.place(x=55,y=150)

		self.coeff_C=Label(root,text="C  : "+str(self.__C),font=("Courier 20 bold"))
		self.coeff_C.place(x=450,y=160)

		self.coeff_gamma=Label(root,text="G  : "+str(self.__gamma),font=("Courier 20 bold"))
		self.coeff_gamma.place(x=450,y=200)

		self.coeff_cv=Label(root,text="CV : 0",font=("Courier 20 bold"))
		self.coeff_cv.place(x=450,y=250)


		self.label_c=Label(root,text="C : ",font=("Courier 20 bold"))
		self.label_c.place(x=28,y=320)

		self.entry_c=Entry(root)
		self.entry_c.insert(END, str(self.__C))
		self.entry_c.place(x=95,y=322, width=80, height=30)

		self.label_gamma=Label(root,text="G : ",font=("Courier 20 bold"))
		self.label_gamma.place(x=200,y=320)

		self.entry_gamma=Entry(root)
		self.entry_gamma.insert(END, str(self.__gamma))
		self.entry_gamma.place(x=270,y=322, width=80, height=30)

		self.coeff_set=Button(root, text="SET", width=10,bg="#ffcccc", fg="black",command= lambda: self.set_coeff())
		self.coeff_set.place(x=380,y=322, width=100, height=30)

		self.train_btn=Button(root, text="Train Model", width=10,bg="#ffcccc", fg="black",command= lambda: self.start_training())
		self.train_btn.place(x=490,y=322, width=180, height=30)


		self.train_btn=Button(root, text="Browse File", width=10,bg="#c1c1c1", fg="black",command= lambda: self.browse_file())
		self.train_btn.place(x=45,y=400, width=180, height=40)


		self.pred_text=Label(root, text="Prediction will be here!",bg="#2C3335",fg="white",font=("Helvetica", 17))
		self.pred_text.place(x=255,y=400,width=400, height=40)

		self.author=Label(root,text="Designed & Developed by - Sam @ 2019",font=("Times 10"))
		self.author.place(x=245,y=480)

	def set_coeff(self):

		c_value = self.entry_c.get()

		g_value = self.entry_gamma.get()

		if re.match("\\d+\\.?\\d+", c_value) and re.match("\\d+\\.?\\d+", g_value):

			if (len(c_value) > 7) or (len(g_value) > 7):
				messagebox.showerror("Error Message", 'Too much length!')
				self.entry_c.delete(0, 'end')
				self.entry_gamma.delete(0, 'end')

			else:
				self.__C = float(c_value)
				self.__gamma = float(g_value)
				self.coeff_C['text'] = "C : " + str(self.__C)
				self.coeff_gamma['text'] = "G : " + str(self.__gamma)
				self.entry_c.delete(0, 'end')
				self.entry_gamma.delete(0, 'end')
		else:
			messagebox.showerror("Error Message", 'Invalid Format!')
			self.entry_c.delete(0, 'end')
			self.entry_gamma.delete(0, 'end')
 
	def browse_file(self):
		if self.__trained == 1:
			self._tempfile = filedialog.askopenfilename(parent=self.parent, initialdir=os.path.join(os.environ["HOMEPATH"], "Desktop"), title='Please Select A Image File',filetypes = (("JPG files","*.jpg"),("JPEG files","*.jpeg"),("PNG files","*.png"),("all files","*.*")))
			self.model.set_path(self._tempfile)
			self.model.rescale_image()
			self.res = self.model.predict()

			self.pred_text["text"]="Predicted Value : "+str(self.res[0])
		else:
			self.pred_text["text"]= "Train The Classifier First!"

	def start_training(self):

		thread = Thread(target = self.train_model(), args = [])
		thread.start()
		# thread.join()

	def train_model(self):

		self.__trained = 1

		# time.sleep(3)

		try:

			self.model = SVMClassifier(c=self.__C, gamma=self.__gamma)
			self.model.train_svm_model()
			self.coeff_cv['text'] = "CV : " + self.model.cross_validation_score()
			messagebox.showinfo("Model Training Info", "Model Trained!")

		except Exception as e:
			self.train_text['text'] = "There were some error! Please try again!"
		
		

