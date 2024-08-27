#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis (World Population Data)

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn


# In[2]:


data = pd.read_csv(r"C:\Users\MANTHAN SHARMA\Downloads\world_population (1).csv")
data


# In[3]:


pd.set_option('display.max.columns', 17)


# In[4]:


pd.set_option('display.float_format', lambda x: '%0.2f' % x)
data


# In[5]:


data.info()


# In[6]:


data.describe()


# In[7]:


data.isnull().sum()


# In[8]:


data.nunique()


# In[9]:


data.duplicated().sum()


# In[10]:


data.sort_values(by = '2022 Population', ascending = False)


# In[11]:


data.corr(numeric_only = True)


# In[12]:


sn.heatmap(data.corr(numeric_only = True), annot = True)


# In[13]:


data.groupby('Continent').mean(numeric_only = True)


# In[14]:


data[data['Continent'].str.contains('Oceania')]


# In[15]:


df = data.groupby('Continent').mean(numeric_only =True).sort_values(by = '2022 Population', ascending = False)
df


# In[16]:


print(plt.style.available)
plt.style.use("classic")


# In[17]:


df.plot(figsize = (18,10))


# In[18]:


df2 = data.groupby('Continent')[['1970 Population', '1980 Population', '1990 Population',
       '2000 Population', '2010 Population', '2015 Population',
       '2020 Population', '2022 Population']].mean(numeric_only =True).sort_values(by = '2022 Population', ascending = False)
df2


# In[19]:


df3 =df2.transpose()
df3


# In[20]:


df3.plot(figsize = (20,10))


# In[ ]:





# In[ ]:





# In[ ]:




