import numpy as np
arr = np.arange(0,11)

print(arr[1])
print(arr[5:9])
arr[5:9] = 100
print(arr[5:9])

arr = np.arange(0,11)
print(arr + arr)
print(arr*arr)
print(5*arr)
print(arr.sum())
print(np.sqrt(arr))
print(np.exp(arr))
print(arr.max())