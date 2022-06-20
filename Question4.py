#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

# Initialise parameters
S0 = 1     # initial stock price
q = 0.5    # the probability of an upwards price movement
r = 0      # interest rate for a signle time period
N = 3      # number of time steps
v = 0.1

def exp_max_Sj(v,N):
    u = 1+v
    for j in range(0,N+1):
        Sj_max = S0 * u ** (np.arange(0,j+1,1))
    weighted_Sj = Sj_max * np.power(q,np.arange(0,N+1,1))
    return sum(weighted_Sj)
       
exp_max_Sj(v,N)


# In[ ]:





# In[ ]:




