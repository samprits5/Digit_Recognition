from tkinter import *
from tkinter import filedialog
from tkinter import font
from machine_learning import SVMClassifier
from threading import Thread
import os
import time


class user_interface(Frame):
	"""docstring for user_interface"""
	def __init__(self, root):

		self._tempfile = ""

		self.__trained = 0

		self.parent = root

		super().__init__(root, width=600, bg="white")
		
		self.algo_text=Label(root,width=40,bg="white",text="Algorithm : SVM Classifier",font=("Helvetica 17 bold"))
		f = font.Font(self.algo_text, self.algo_text.cget("font"))
		f.configure(underline=True)
		self.algo_text.configure(font=f)
		self.algo_text.pack(side=TOP,pady=10,padx=15,ipadx=8,ipady=8)

		self.train_text=Label(root,text="Use The Button Below To Train Model",font=("Helvetica", 17))
		self.train_text.pack(side=TOP, pady=10,padx=15,ipadx=8,ipady=8)

		self.train_btn=Button(root, text="Train Model", width=10,bg="#ffcccc", fg="black",command= lambda: self.start_training())
		self.train_btn.pack(side=TOP,padx=5,pady=5,ipadx=8,ipady=8)

		self.pred_text=Label(root, text="Prediction will be here!",width=40,bg="cyan",font=("Helvetica", 17))
		self.pred_text.pack(side=TOP,pady=10,padx=15,ipadx=8,ipady=8)

		self.browse_btn=Button(root, text="Browse File", width=10,bg="#ffcccc", fg="black",command= lambda: self.browse_file())
		self.browse_btn.pack(side=TOP,padx=5,pady=5,ipadx=8,ipady=8)

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

		self.train_text['text'] = "Training model..."
		thread = Thread(target = self.train_model(), args = [])
		thread.start()
		# thread.join()

	def train_model(self):

		self.__trained = 1

		# time.sleep(3)

		try:

			self.model = SVMClassifier(c=1000, gamma=0.22)
			self.model.train_svm_model()
			self.train_text['text'] = "Model Trained. C = " + self.model.get_C() + " , Gamma = " + self.model.get_gamma() + " , Score = " + self.model.cross_validation_score()

		except Exception as e:
			self.train_text['text'] = "There were some error! Please try again!"
		
		

