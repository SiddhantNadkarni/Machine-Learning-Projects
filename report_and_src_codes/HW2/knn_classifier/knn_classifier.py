from sklearn.neighbors import KNeighborsClassifier
import numpy as np

class knnclassifier(object):
	"""This class performs KNN classifier and returns 
    predicted value, errors"""
	def __init__(self, x_train, y_train, x_test, y_test, k_val, p_val):
		super(knnclassifier, self).__init__()
		self.k_val = k_val
		self.p_val = p_val
		self.x_train = x_train
		self.x_test = x_test
		self.y_train = y_train
		self.y_test = y_test
		self.knn = KNeighborsClassifier(n_neighbors = self.k_val, p = self.p_val)
		self.knn.fit(x_train, y_train)
		self.y_test_predicted = self.knn.predict(self.x_test)
		self.y_train_predicted = self.knn.predict(self.x_train)


	def get_y_test_pred(self):
		return self.y_test_predicted

	def get_y_train_pred(self):
		return self.y_train_predicted

	def computeErrorTest(self):
		return (np.sum(abs(self.y_test - self.y_test_predicted))/len(self.y_test))

	def computeErrorTrain(self):
		return np.float128(np.sum(abs(self.y_train - self.y_train_predicted))/len(self.y_train))


		






		