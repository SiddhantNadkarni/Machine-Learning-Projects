import numpy as np


class performanceMeasure(object):
	"""This class takes in the predicted and true values and returns all the
	accuracy score measures such as F-1 score, error rate"""
	def __init__(self, y_true, y_pred):
		self.y_true = y_true
		self.y_pred = y_pred

		self.TP = 0
		self.FP = 0
		self.TN = 0
		self.FN = 0

		for i in range(len(y_true)):
		    if y_true[i] == y_pred[i] == 1:
		        self.TP +=1
		    if y_true[i] == y_pred[i] == 0:
		        self.TN +=1
		    if y_true[i] == 0 and y_pred[i] == 1:
		        self.FP +=1
		    if y_true[i] == 1 and y_pred[i] == 0:
		        self.FN+=1

		self.TPR = self.TP/(self.TP + self.FN)
		self.TNR = self.TN/(self.TN + self.FP)
		self.PPV = self.TP/(self.TP + self.FP)
		self.F1score = 2*(self.PPV*self.TPR)/(self.PPV + self.TPR) 

	def get_performance_measure(self):
		return (self.TP, self.TN, self.FP, self.FN)

	def get_F1score(self):
		return self.F1score

	def get_errorRate(self):
		self.accuracy = (self.TP + self.TN)/(self.TP + self.TN + self.FP + self.FN)
		self.error_rate = 1 - self.accuracy
		return self.error_rate

	def get_confusion_matrix(self):
		self.confusion_matrix = [[self.TP, self.FP], [self.FN, self.TN]]
		return self.confusion_matrix




		