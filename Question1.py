#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np


# In[12]:


# Initialise parameters
S0 = 1     # initial stock price
q = 0.5    # the probability of an upwards price movement
K = 1.05   # strike price
r = 0      # interest rate for a signle time period
N = 3      # number of time steps
v = 0.1

def binomial_tree_eurcall(v,K,N,r):
    u = 1+v
    d = 1-v
    disc = np.exp(-r*N)
    
    S = np.zeros(N+1)
    S[0] = S0*d**N
    for j in range(1,N+1):
        S[j] = S[j-1]*u/d
    
    C = np.zeros(N+1)
    for j in range(0,N+1):
        C[j] = max(0, S[j]-K)  
    
    # step backwards through tree
    for i in np.arange(N,0,-1):
        for j in range(0,i):
            C[j] = disc * ( q*C[j+1] + (1-q)*C[j] )
    return C[0]
        
binomial_tree_eurcall(v,K,N,r)


# In[13]:


def binomial_tree_eurcall2(v,K,N,r):
    #precompute constants
    u = 1+v
    d = 1-v
    disc = np.exp(-r*N)
    
    # initialise asset prices at maturity - Time step N
    C = S0 * d ** (np.arange(N,-1,-1)) * u ** (np.arange(0,N+1,1)) 

    # initialise option values at maturity
    C = np.maximum( C - K , np.zeros(N+1) )
        
    # step backwards through tree
    for i in np.arange(N,0,-1):
        C = disc * ( q * C[1:i+1] + (1-q) * C[0:i] )
    return C[0]


# In[10]:


binomial_tree_eurcall2(v,K,N,r)


# In[ ]:





# In[ ]:





# In[ ]:




