
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
df=pd.read_csv("house1.csv")
df.head()


# In[20]:


df.drop(['Unnamed: 0'],axis=1,inplace=True)
df


# In[21]:


import joblib
p=joblib.load("houses.joblib")


# In[22]:


df


# In[23]:


result=p.predict(df)
result


# In[24]:


print(result[0])

