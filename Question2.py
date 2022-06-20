#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np

# Initialise parameters
S0 = 1     # initial stock price
q = 0.5    # the probability of an upwards price movement
K = 1.05   # strike price
r = 0      # interest rate for a signle time period
N = 3      # number of time steps
v = 0.1

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

def goal_seek(target,_threshold):
    threshold = _threshold
    lower = 0
    upper = 10
    solve = (lower + upper)/2
    while abs(threshold) >= _threshold:
        threshold = target - binomial_tree_eurcall2(solve,K,N,r)
        if threshold < 0:
            upper = solve
            solve = (lower + upper)/2
        elif threshold > 0:
            lower = solve
            solve = (lower + upper)/2        
            
    return solve

# example
# goal_seek(0.0497500000000001,0.000001)


# In[ ]:





# In[ ]:





# In[ ]:




