import numpy as np
L =  [1,2,3]
A = np.array([1,2,3])
L.append(4)
print (L)
print (A)
print (L+L)
print (A+A)
radToDegree = 57.2958
a = np.array([1,2])
b = np.array([2,1])
dot = 0
for e,f in zip (a,b):
	dot = dot + e*f 
print (dot)
print (a*b)
print (np.sum(a*b))
print ((a*b).sum())

amag = np.sqrt((a*a).sum())
bmag = np.sqrt((b*b).sum())
mag = amag * bmag
magNorm = np.linalg.norm(a) * np.linalg.norm(b)
print (mag)
print (magNorm)
cosTheta = ((a.dot(b))/(magNorm))
theta = np.arccos(cosTheta)
print (theta*radToDegree)
cosTheta = ((a.dot(b))/(mag))
theta = np.arcsin(cosTheta)
print (theta*radToDegree)


L = [[1,2],[3,4]]
M = np.array(L)
print (M[0][0])
print (L[0][0])
M2 = np.matrix(L)
oneto100 = np.array(list(range(1,100)))
zeroarr = np.zeros((10,10))
onesarr = np.ones ((10,10))
np.arange()