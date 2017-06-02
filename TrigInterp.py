import numpy as np
import matplotlib.pyplot as plt

def TrigInterp(x,y,Nnew):
    #Trigonometric Interpolation
    #Input
    #x = Interpolation nodes (vector of length N)
    #y = Interpolation nodes (Vector of length N)
    #Nnew = New length of the data vector
    #Output
    #P = New vector of appropriate length Nnew
    
    #Define out interpolation points
    N=len(x)
    xi = np.linspace(x[0],x[N-1],Nnew)
    h=2/N
    scale = (x[2]-x[1])/h
    x = x/scale
    xi = xi/scale
    
    #evaluate the interpolation points
    P = np.zeros(Nnew)
    
    for k in range(N):
        P = P + y[k]*TrigInt(xi-x[k],N)
    
    return P
            
    
    

