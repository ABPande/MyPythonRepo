import numpy as np 
import pandas as pd 

d = {
	'A': "foo foo foo bar bar bar".split(),
	'B': "one one two two one one".split(),
	'C': "x y x y x y".split(),
	'D': [1,3,2,5,4,1]
	}
df = pd.DataFrame(d)
print(d)
print(df['A'].unique())
print(df['A'].value_counts())
print (df.pivot_table(values='D', 
	index = ['A','B'],
	 columns = ['C']))
groupbyA = df.groupby('A')
print(groupbyA.D.max())

