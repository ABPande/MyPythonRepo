import numpy as np
zeroarr = np.zeros(10)
print(zeroarr)
arr10to50 = np.arange(10,51,2)
print(arr10to50)
mat3x3 = np.arange(0,9)
mat3x3 = mat3x3.reshape(3,3)
print(mat3x3)
identmat = np.eye(3)
print(identmat)
print (np.random.rand(1))
print (np.random.randn(1,25))
print (np.linspace(0.01,1,100).reshape(10,10))
print (np.linspace(0,1,20))

mat5x5 = np.arange(1,26).reshape(5,5)
print (mat5x5[2:,1:])
print (mat5x5[3,4])
print (mat5x5[:3,1:2])
print (mat5x5[4:,:])
print (mat5x5[3:,:])
print (np.sum(mat5x5))
print (np.std(mat5x5))
print (mat5x5)
print (mat5x5.sum(axis = 1))