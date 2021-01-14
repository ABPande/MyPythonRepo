import random
def numGen(num):
	for item in range(1, num+1):
		yield item**3

def funcGenCall(num):
	for item in numGen(num):
		print(item)

def funcRandGenCall(startNum, endNum, count):
	for item in range (0,count):
		print(randGen(startNum, endNum))

def randGen(startNum, endNum):
	return(random.randint(startNum, endNum))

def returnIter(stringToIter):
	return iter(stringToIter)

def printStr(stringToPrint):
	stringIter = returnIter(stringToPrint)
	for item in list(stringToPrint):
		print (next(stringIter))

funcGenCall(10)
funcRandGenCall(8,20,4)
printStr("SuperNatural")
