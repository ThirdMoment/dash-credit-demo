
# coding: utf-8

# In[32]:


import pandas as pd
import plotly
import plotly.plotly as py
from plotly.graph_objs import *
import matplotlib.pyplot as plt
import plotly.tools as tls


# In[ ]:


plotly.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')


# In[87]:


df = pd.read_csv('../data/cs-training.csv')
del df['Unnamed: 0']


# In[22]:



for column in df.columns.values:
    if "" in column:
        df[column].fillna(df[column].mean(), inplace=True)


# In[26]:


df = df.dropna()


# In[89]:


for column in df.columns.values:
    data_bar_charts = {}
    x = df.groupby('SeriousDlqin2yrs', as_index=False)[column].mean()
    data_bar_charts = dict(zip(x[0], x[1]))
    print(x)
    


# In[69]:


te = {}


# In[ ]:





# In[99]:


te = df.groupby('SeriousDlqin2yrs', as_index=False)['MonthlyIncome'].mean()


# In[112]:


zip(te.iloc[0]).__next__()


# In[77]:


dict(zip(x['NumberOfDependents'], x['SeriousDlqin2yrs']))

x.columns[0]


# In[57]:


x = {'0': {
    'NumberOfDependents': df.NumberOfDependents.mean()
    
}}
x


# In[76]:


df.groupby('SeriousDlqin2yrs').apply(lambda x: dict(zip(x['SeriousDlqin2yrs'], x['NumberOfDependents'].mean())).to_dict())


# In[51]:


print (df.groupby(level='ISBN')
         .apply(lambda x: dict(zip(x['User-ID'], x['Book-Rating'])))
         .to_dict())


# In[46]:


x


# In[40]:


df.groupby('SeriousDlqin2yrs', as_index=True)['age'].mean()


# In[ ]:




