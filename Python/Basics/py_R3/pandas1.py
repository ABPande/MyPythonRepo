import pandas as pd
import numpy as np

labels = ['a','b','c']
mylist = [10,20,30]

arr = np.array(mylist)
d = {'a':10, 'b':20, 'c':30}

pdarr1 = pd.Series(data = mylist)
pdarr2 = pd.Series(data = mylist, index = labels)
print (pdarr1)
print (pdarr2)
pdarr3 = pd.Series(d)
print (pdarr3)

from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print (df)
print (df[['W','Z']])
df['U'] = df['W'] + df ['Z']
print (df['U'])
print (df.drop('U',axis = 1))
print(df)
df.drop('U',axis = 1,inplace = True)
print (df)
print(df.loc['C':,'Y':])


