import numpy as np
import matplotlib.pyplot as plt

#x - x data
#y - y data
#s - Shift (fraction of a data point) 
#note: (+s) shifts left, (-s) shifts right

def FFTShift(x,y,s):
    
    #Compute Fourier Transform of y data
    fty = np.fft.fft(y)
    m = np.fft.fftfreq(len(y))
    
    #Compute Appropriate Phase factor for Shift Theorem
    phase = np.exp(2*np.pi*m*1j*s)
    
    #Compute Shifted y data
    Y = np.fft.ifft(fty*phase)
    step = (x[1]-x[0])
    X = x - s*step
    
    return X,Y
    
    
    #Allows you to ensure the Standard deviation remains the same through this process
    #c=y.std()
    #d=y2.std()
    #return c,d

    