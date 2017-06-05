import numpy as np 
import matplotlib.pyplot as plt

def TrigInt(x,N):
    
    #This function evaluates the interpolation points
    
    if N % 2 == 1: #odd
        tau = np.sin(N*np.pi*x/2)/(N*np.sin(np.pi * x/2))
    else: #even
        tau = np.sin(N*np.pi*x/2)/(N*np.tan(np.pi*x/2))
        
        tau[x==0] = 1
    return tau

