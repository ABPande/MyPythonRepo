#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xlrd


# In[3]:


import pandas as pd

dfCsv = pd.read_csv("C://MLData/example.csv")

print (dfCsv)
dfCsv.to_excel("C://MLData/exampleoutput.xlsx", sheet_name = "SheetOutput", index = False)
dfExcel = pd.read_excel("C://MLData/exampleoutput.xlsx", sheet_name = "SheetOutput")
print (dfExcel)


# In[ ]:




