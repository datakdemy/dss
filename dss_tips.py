#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dataiku
from dataiku import pandasutils as pdu
import pandas as pd

client = dataiku.api_client()

# Get a list of Project Keys
project_keys = client.list_project_keys()

project_keys
project = client.get_project("ANALYSE_ECOMMERCE")


# In[ ]:




