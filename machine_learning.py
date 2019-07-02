
import numpy as np
from PIL import Image
from sklearn import datasets, svm
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import cross_val_score




class SVMClassifier(object):
	"""docstring for SVMClassifier"""
	def __init__(self, c=100, gamma=0.20):
		self._path = ""
		self._C = c
		self._gamma = gamma

	def get_C(self):
		return str(self._C)

	def get_gamma(self):
		return str(self._gamma)

	def set_path(self, path):
		self._path = path

	def rescale_image(self):

	    scaler2 = MinMaxScaler()

	    img = Image.open(self._path).convert('L')
	    
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

	    self._scaledList = scaler2.transform(myLi).reshape(1,-1)

	def train_svm_model(self):
    
	    self.digits = datasets.load_digits()
	    scaler = MinMaxScaler()
	    n_samples = len(self.digits.images)
	    self.data = self.digits.images.reshape((n_samples, -1))
	    scaler.fit(self.data)
	    self.data = scaler.transform(self.data)
	    
	    self._classifier = svm.SVC(gamma=self._gamma, C=self._C)
	    
	    self._classifier.fit(self.data, self.digits.target)

	def cross_validation_score(self):

		return str(round(cross_val_score(self._classifier, self.data, self.digits.target, cv=5).mean(),2))


	def predict(self):

		return self._classifier.predict([self._scaledList[0]])

		