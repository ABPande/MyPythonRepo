mylist = [1,2,3]
listoflists= [[1,2,3],[4,5,6],[7,8,9]]
import numpy as np
arr = np.array(mylist)
print (arr)
matarr = np.array(listoflists)
print (matarr)
nprangearr = np.arange (0,11,2)
print (nprangearr)
npzerosarr = np.zeros(3)
print (npzerosarr)
npmatzeros = np.zeros((2,3))
print (npmatzeros)
evenlyspacedarr = np.linspace (0,5,100)
print (evenlyspacedarr)
identmat=np.eye(4)
print (identmat)
randommat = np.random.rand(3,4)
print (randommat)
randomnormalmat = np.random.randn(4,4)
print (randomnormalmat)
randomarr=np.random.randint(1,101,10)
print (randomarr)
mylist = [1,2,3]

import numpy as np
mylistarr  = np.array(mylist)
print (mylistarr)
arrmat = np.array(listoflists)
print (mylistarr)
arangearr = np.arange(0,11,3) #11 to include 10
print (arangearr)
arrzeros = np.zeros((5,6))
print (arrzeros)
evenlyspacedarr = np.linspace(0,5,10)
print (evenlyspacedarr)
identitymatrix = np.eye(4)
print (identitymatrix)
randU = np.random.rand(3,4) #uniform distribution
print (randU)
randN = np.random.randn(3,4)#normal distribution
print (randN)
random10numbers =  np.random.randint (0,100,10) #10 is number of integers
print (random10numbers)
arr = np.arange(25)
print (arr)
ranarr = np.random.randint(0,50,10)
print (ranarr)
reshapedarr = ranarr.reshape (2,5)
print (reshapedarr)

arr = np.arange(0,11)
print(arr[0])
arrcopy = arr.copy()