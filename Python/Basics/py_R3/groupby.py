import numpy as np 
import pandas as pd 

data = {'Company': "GOOG GOOG MSFT MSFT FB FB".split(),
		'Person': "Sam Charlie Amy Vanessa Carl Sarah".split(),
		'Sales': [200,120,340,124,243,350]}

df = pd.DataFrame(data)
df['Sales'].fillna(value=df['Sales'].mean(), inplace = True)
print (df)

bycomp = df.groupby("Company")
print (bycomp)
print (bycomp.sum().loc['FB'])
print (bycomp.describe().loc['GOOG'])