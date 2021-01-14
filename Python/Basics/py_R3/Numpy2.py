import numpy as np
nparr = np.array([1,2,3,4])
print(nparr.sum())
nparr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
npgenarr = np.arange(0,100)
npreshapedarr = npgenarr.reshape(10,10)
npzerosarr = np.zeros((3,3))
nponesarr = np.ones((3,3))
nplinspacearr = np.linspace(0,10,100)
print(nparr2d)
print(nplinspacearr)
print (npgenarr)
print (npreshapedarr)

print(np.random.rand(4,4))
print(np.random.randn(4,4))
print(np.random.randint(1,100,10))

