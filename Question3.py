#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

# Initialise parameters
S0 = 1     # initial stock price
q = 0.5    # the probability of an upwards price movement
K = 1.05   # strike price
r = 0      # interest rate for a signle time period
N = 3      # number of time steps
v = 0.1

def binomial_tree_amercall(v,K,N,r):
    #precompute constants
    u = 1+v
    d = 1-v
    disc = np.exp(-r*N)
    
    # initialise asset prices at maturity - Time step N
    S = S0 * d ** (np.arange(N,-1,-1)) * u ** (np.arange(0,N+1,1)) 
    
    # option payoff 
    C = np.maximum(0, S - K)
    
    # backward recursion through the tree
    for i in np.arange(N-1,-1,-1):
        S = S0 * d**(np.arange(i,-1,-1)) * u**(np.arange(0,i+1,1))
        C[:i+1] = disc * ( q*C[1:i+2] + (1-q)*C[0:i+1] )
        C = C[:-1]
        C = np.maximum(C, S - K)
            
    return C[0]

binomial_tree_amercall(v,K,N,r)


# In[ ]:





# In[ ]:




