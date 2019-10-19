import pandas as pd
import numpy
import glob
import os
from natsort import natsorted

class DataLoader(object):
	"""docstring for DataLoader"""
	def __init__(self, path):
		self.path = path
		self.activities = natsorted(glob.glob(self.path + '/[!.pdf]*'))
		self.instance_of_activity = []
		self.finalFiles = pd.DataFrame()

		for activity in self.activities:
			self.instances = natsorted(glob.glob(activity + '/*'))
			for instance in self.instances:
				self.instance_of_activity.append(instance)

		for x in self.instance_of_activity:
			files = pd.read_csv(x, skiprows = 4)
			files = files.rename(columns = {"# Columns: time": "time"})
			self.finalFiles = self.finalFiles.append(files)

	def getActivities(self):
		return self.activities
	def getActivityInstances(self):
		return self.instance_of_activity
	def getFinalDataFrame(self):
		return self.finalFiles
	def testTrainSplit(self):
		self.testDF = pd.DataFrame()
		self.trainDF = pd.DataFrame()
		self.classBinTest = []
		self.classMulTest = []
		self.classBinTrain = []
		self.classMulTrain = []
		self.activities = (glob.glob(self.path + '/*'))
		for activityPath in self.activities:
			self.testDFList = []
			self.trainDFList = []
			if activityPath.split('/')[-1] == 'bending1' or activityPath.split('/')[-1] == 'bending2':
				self.testLen = 2
				self.instances = natsorted(glob.glob(activityPath + '/*'))
				for x in range(0, self.testLen):
					self.testDFList.append(self.instances[x])
					self.classBinTest.append(1)
					self.classMulTest.append(activityPath.split('/')[-1])
				for x in range(len(self.testDFList)):
					files = pd.read_csv(self.testDFList[x], skiprows = 4)
					files = files.rename(columns = {"# Columns: time": "time"})
					self.testDF = self.testDF.append(files)
				for x in range(self.testLen, len(self.instances)):
					self.trainDFList.append(self.instances[x])
					self.classBinTrain.append(1)
					self.classMulTrain.append(activityPath.split('/')[-1])
				for x in range(len(self.trainDFList)):
					files = pd.read_csv(self.trainDFList[x], skiprows = 4)
					files = files.rename(columns = {"# Columns: time": "time"})
					self.trainDF = self.trainDF.append(files)
			else:
				self.testLen = 3
				self.instances = natsorted(glob.glob(activityPath + '/*'))
				for x in range(0, self.testLen):
					self.testDFList.append(self.instances[x])
					self.classBinTest.append(0)
					self.classMulTest.append(activityPath.split('/')[-1])
				for x in range(len(self.testDFList)):
					files = pd.read_csv(self.testDFList[x], skiprows = 4)
					files = files.rename(columns = {"# Columns: time": "time"})
					self.testDF = self.testDF.append(files)
				for x in range(self.testLen, len(self.instances)):
					self.trainDFList.append(self.instances[x])
					self.classBinTrain.append(0)
					self.classMulTrain.append(activityPath.split('/')[-1])
				for x in range(len(self.trainDFList)):
					files = pd.read_csv(self.trainDFList[x], skiprows = 4)
					files = files.rename(columns = {"# Columns: time": "time"})
					self.trainDF = self.trainDF.append(files)
		return (self.trainDF, self.testDF, self.classBinTrain, self.classBinTest, self.classMulTrain, self.classMulTest)

def main():
	dataPath = '../Homework_3_Data/AReM/'
	dataLoader = DataLoader(dataPath)
	trainDF, testDF = dataLoader.testTrainSplit()
	print(trainDF.shape)
	print(testDF.shape)

if __name__ == '__main__':
	main()
	print('Done')
