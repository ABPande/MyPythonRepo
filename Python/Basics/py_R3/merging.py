import numpy as np
import pandas as pd

d1 = {
'c1':[1,2,3,4],
'c2':[444,555,666,444],
'c3':'abc def hij lmn'.split()}

d2 = {
	'c1':[1,2,3],
	'c4':'x y z'.split()
	}
print (d1)
df1 = pd.DataFrame(d1)
print (df1)
print(df1['c2'].unique())
df2 = pd.DataFrame(d2)
print (pd.merge(df1,df2,how="inner",on='c1'))

print (df1['c2'].value_counts())
print (df1.index.names )