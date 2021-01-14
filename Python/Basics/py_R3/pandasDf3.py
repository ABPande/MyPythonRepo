import numpy as np 
import pandas as pd 

outside = "G1 G1 G1 G2 G2 G2".split()
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(outside)
df = pd.DataFrame(np.random.randn(6,2),hier_index,['A','B'])
print(df)
print (df.loc['G2'].loc[1]['B'])
