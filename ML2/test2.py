
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
def predict():
    df=pd.read_csv("ML/house2.csv")
    df.head()


    # In[20]:


    df.drop(['Unnamed: 0'],axis=1,inplace=True)
    df


    # In[21]:


    import joblib
    p=joblib.load("ML/houses.joblib")


    # In[22]:


    df


    # In[23]:


    result=p.predict(df)
    result


    # In[24]:


    print(result[0])
    return(result)

