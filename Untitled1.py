
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


x = np.array([1,2,0,0,4,0])
a= x[x>0]
a


# In[3]:


y = np.random.random(10)


# In[4]:


y


# In[7]:


y.sort()


# In[8]:


y


# In[16]:


import numpy as np
def sigmoid(x):
    y= (1)/(1+ np.exp(-x))
    return y


# In[17]:


x=[[1,2,3],[4,5,6]]


# In[18]:


y


# In[19]:


sigmoid(10)


# In[20]:


sigmoid(2)


# In[23]:


import numpy as np
x= np.zeros((5,5))
x


# In[24]:


x[1:-1,1:-1] += 1


# In[25]:


x


# In[26]:


x


# In[27]:


import numpy as np
x= np.zeros((5,5))
x


# In[30]:


a= np.array([1,2,3,2,3,4,3,4,5,6])
b= np.array([7,2,10,2,7,4,9,4,9,8])
y= a-b
np.where(y==0)


# In[2]:


import pandas as pd 
df = pd.read_csv("ign.csv")


# In[3]:


df.head()


# In[41]:


platform = df[(df['editors_choice'] == 'Y') & (df["score"]>9) & (df["release_year"]>2015)]


# In[42]:


platform["platform"].value_counts()


# In[43]:


import pandas as pd 
df = pd.read_csv("ign.csv")


# In[44]:


df


# In[52]:


df2= df.groupby(by=['platform','score']).mean()


# In[53]:


df2.sort_values('release_year')

