#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np

# Initialise parameters
S0 = 1      # initial stock price
q = 0.5     # the probability of an upwards price movement
K = 1.05    # strike price
r = 0       # interest rate for a signle time period
N = 3       # number of time steps
v = 0.1

def binomial_tree_amercall(v,K,N,r):
    #precompute constants
    u = 1+v
    d = 1-v
    disc = np.exp(-r*N)
    
    V = []
    for j in range(0,N+1):
        # initialise asset prices at maturity - Time step N
        C = S0 * d ** (np.arange(j,-1,-1)) * u ** (np.arange(0,j+1,1)) 
        
        # initialise option values at maturity
        C = np.maximum( C - K , np.zeros(j+1) )

        # step backwards through tree
        for i in np.arange(j,0,-1):
            C = disc * ( q * C[1:i+1] + (1-q) * C[0:i] )
        V.append(C[0])
    return max(V)


# In[6]:


binomial_tree_amercall(v,K,N,r)


# In[ ]:





# In[ ]:




