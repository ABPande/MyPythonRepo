import pandas as pd
import numpy as np
labels = ['a','b','c']
mydata = [10,20,30]
arr = np.array(mydata)
d = {'a':10, 'b':20, 'c':30}
mydataseries = pd.Series(data =mydata, index = labels)
arrseries = pd.Series(arr,labels)
dseries = pd.Series(d)

print (mydataseries)
print (arrseries)
print (dseries)

countryseries = pd.Series ([1,2,3,4],['USA','INDIA','JAPAN','UNITED KINGDOM'])
print (countryseries)
print (countryseries['USA'])


from numpy.random import randn

np.random.seed(22)
print(randn(5,4))
print (randn(5))
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print (df)

print(df[['Z','W']])

df['U'] = df['W'] - df ['X']
print(df)
dfDropped = df.drop('U',axis=1)
print(df)
print(dfDropped)
#df.drop['U',axis = 1, inplace=True]
