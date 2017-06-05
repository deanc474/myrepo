import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

def TrigInterp(x,y,Nnew):
    #Trigonometric Interpolation
    #Input
    #x = Interpolation nodes (vector of length N)
    #y = Interpolation nodes (Vector of length N)
    #Nnew = New length of the data vector
    #Output
    #P = New vector of appropriate length Nnew
    
    #Note This function does not output an x vector.
    
    #Define out interpolation points
    N=len(x)
    X = np.linspace(x[0],x[N-1],Nnew)
    y = np.asmatrix(y) #Necessary for matrix multiplication
    
    xi = np.linspace(x[0],x[N-1],Nnew)#New x data points
    
    h=2/N 
    scale = (x[2]-x[1])/h 
    x = x/scale
    x=np.asmatrix(x) #Necessary for matrix multiplication
    xi = xi/scale
    xi = np.asmatrix(xi) #Necessary for matrix multiplication
    
    #evaluate the interpolation points
    Y = np.zeros(Nnew)
    Y = np.asmatrix(Y)
    
    
    #To avoid using a for loop we instead use matrix multiplication
    
    h=np.ones(N)
    h=np.asmatrix(h)
    k=np.ones(Nnew)
    k=np.asmatrix(k)
    
    Y = Y + np.dot(y,TrigInt(np.transpose(np.dot(np.transpose(xi),h))-np.dot(np.transpose(x),k),N))
    # [1xNnew] = [1xNnew] + [1xN] * (([1xNnew]'*[1xN])' - ([1xN]'*[1xNnew]))
    # [1xNnew] = [1xNnew] + [1xN] * [NxNnew]
    Y = np.transpose(Y)

    
    return X,Y
    
    

