import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

def FTExp(x,y,Nfactor): #Accepts Equally spaced x data points   Nfactor integer!!
    N = len(x)
    Nnew = Nfactor*N
    S = Nnew - N
    
    #Take the fast fourier transform, and represent as a matrix
    fty = np.fft.fft(y)
    m = np.fft.fftfreq(len(x))
    fty = np.asmatrix(fty)
    
    #Determine where m changes sign
    zeros = np.where(np.diff(np.sign(m)))[0]
    cross=zeros[len(zeros)-1] #Cross is the element number where the cross from positive to negative occurs
    m = np.asmatrix(m)
    
    #Create the Expanding Matrix (to add the appropriate number of zeroes)
    A = np.eye(N,cross + 1)
    B = np.zeros([N,S])
    rem = len(x) - (cross + 1)
    C = np.eye(N,rem,-(N-rem))
    D = np.concatenate((A,B,C), axis=1) # D is the expanding matrix
    
    #Create the new vectors
    
    FTY = np.dot(fty,D)
    FTY = np.squeeze(np.asarray(FTY))
    
    #Inverse Fourier Transform back
    Y = Nfactor*np.fft.ifft(FTY)
    step = (x[1]-x[0])/Nfactor
    X = np.arange(x[0],x[len(x)-1]+2*step,step)
    
    #Ensure X is the correct length
    k = len(X)
    l = len(Y)
    X = np.dot(X,np.eye(k,l))
    
    #If you want to demonstrate the Interpolation
    #plt.figure(1)
    #plt.plot(X,Y.real,'bo',x,y,'r*')
    
    return X,Y