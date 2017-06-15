import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

def FTCont(x,y,Nnew): #Accepts Equally spaced x data points Nnew is EVEN!!
    
    #Only works if len(x) is Even/Odd, then Nnew also has to be Even/Odd.
    N = len(x)
    S = N - Nnew
    half = S/2
    
    
    #Take the fourier transform
    fty = np.fft.fft(y)
    fty = np.asmatrix(fty)
    m = np.fft.fftfreq(N)
    
    #Determine where m changes sign
    zeros = np.where(np.diff(np.sign(m)))[0]
    cross=zeros[len(zeros)-1] #Cross is the element number where the cross from positive to negative occurs
    m = np.asmatrix(m)
    
    #Create a Contraction matrix
    A = np.eye(N,cross + 1 - half)
    B = np.eye(N,N-(cross+1)-half,-(cross+1)-half)
    D = np.concatenate((A,B), axis=1) # D is the expanding matrix
    
    #Perform the reduction
    FTY = np.dot(fty,D)
    FTY = np.squeeze(np.asarray(FTY))
    
    #Take the inverse fourier transform
    factor = Nnew/N
    Y = factor*np.fft.ifft(FTY)
    step = (x[1]-x[0])/factor
    X = np.arange(x[0],x[len(x)-1],step)
    
    #Ensure X is the correct length
    k = len(X)
    l = len(Y)
    X = np.dot(X,np.eye(k,l))
    
    
    return X,Y