#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
x = np.linspace(0,5,11)
y = x ** 2


# In[2]:


plt.plot(x,y,'r-')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("X vs Y")
plt.show()


# In[3]:


plt.subplot(1,3,1)
plt.plot(x,y,'r')
plt.subplot(1,3,2)
plt.plot(y,x,'b')
plt.subplot(1,3,3)
plt.plot(y,x ** .4,'g')
plt.show()


# In[4]:


fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.set_xlabel("X Label")
axes.set_ylabel("Y Label")
axes.plot(x,y)


# In[5]:


fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.4,0.4,0.42,0.42])
axes2.set_xlabel("X")
axes2.set_ylabel("Y")
axes1.plot()
axes2.plot()
axes1


# In[12]:


fig1,axes = plt.subplots(nrows = 1, ncols = 2)
axes[0].plot(x,y)
axes[1].plot(x,y)


# In[ ]:





# In[ ]:




