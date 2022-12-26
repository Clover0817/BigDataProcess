import numpy as np
import sys
import os
import operator

def createDataSet(trainingDir):
	files = os.listdir(trainingDir)
	
	group = [0 for i in range(len(files))]
	labels = []

	i = 0
	for fname in files:
		data = []
		file = trainingDir + "/" + fname 
		labels.append(int(fname[0]))
        
		f = open(file)
		for line in f.readlines():
			for c in line:
				if c == '0' or c == '1':
					data.append(int(c))
		group[i] = data
		i += 1
	
	dataSet= np.array(group)

	return dataSet, labels

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]



trainingDir = str(sys.argv[1])
testDir = str(sys.argv[2])
dataSet, labels = createDataSet(trainingDir)
test = os.listdir(testDir)
allData = len(test)

for k in range(20):
	failed = 0

	for fname in test:
		data = []
		file = testDir + "/" + fname
		answer = int(fname[0])

		f = open(file)
		for line in f.readlines():
			for c in line:
				if c == '0' or c == '1':
					data.append(int(c))	

		inX = np.array(data)
		result = classify0(inX, dataSet, labels, k+1)

		if result != answer:
			failed += 1

	error = failed / allData * 100
	print(round(error))