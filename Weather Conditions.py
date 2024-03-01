#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd 


# In[14]:


df = pd.read_csv(r"C:\Users\juani\OneDrive\Desktop\PYTHON\myexercises\power\file.csv")
df


# In[15]:


df.head(10)


# In[16]:


df.shape


# In[17]:


df.index


# In[19]:


df.columns


# In[21]:


df.dtypes


# In[27]:


df['Weather'].unique()


# In[28]:


df.nunique()


# In[29]:


df.count()


# In[31]:


df['Weather'].value_counts()


# In[32]:


·df.info()


# In[33]:


df.head(2)


# In[48]:


df['Wind Speed_km/h'].nunique()


# In[46]:


#
df['Wind Speed_km/h'].unique()


# In[47]:


df[df['Wind Speed_km/h'] == 4]


# In[ ]:





# In[ ]:





# In[39]:


#
df.Weather.value_counts()


# In[49]:


#
df.groupby('Weather').get_group('Rain')


# In[56]:


##########
df.isnull().sum()


# In[59]:


df = df.dropna()


# In[60]:


df.isnull().sum()


# In[67]:


df.rename(columns = { 'Weather' : 'Weather Condition',
                      'Press_kPa' : 'kilopascal',
                      'Visibility_km' :  'Visibilitykm',
                      'Wind Speed_km/h' : 'Wind Speed',
                      'Rel Hum_%' : 'Rel Hum_%',
                      'Dew Point Temp_C%' : 'Dew Point temperature',
                      'Rel Hum_%' : 'Rel Hum_%',
                      'Temp_C' : 'Temperature',
                      'Date/Time' : 'Daytime',
                    }, inplace=False)


# In[68]:


##########find all instances when wind speed is above 24 and visibility is 25


# In[73]:


df[(df['Wind Speed'] > 24) & (df['Visibilitykm' ] == 25 )]


# In[74]:


df.groupby('Weather Condition').mean()


# In[78]:


df.groupby('Temperature').max()


# In[77]:


df.groupby('Temperature').min()


# In[80]:


df.groupby('Weather Condition').get_group('Fog')


# In[81]:


df[(df['Weather Condition'] == 'Clear ') | (df['Visibilitykm'] > 40 )]


# In[84]:


df[(df['Weather Condition'] == 'Clear ') & (df['Rel Hum_%'] > 50 ) | (df['Visibilitykm'] > 40 )]


# In[ ]:




