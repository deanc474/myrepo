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
    y2 = np.fft.ifft(fty*phase)
    
    #Plot the figure
    plt.figure(1)
    plt.hold(True)
    a=plt.plot(x,y2.real)
    #b=plt.plot(x,y, label = 'Original')
    plt.hold(False)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('FFT Shift')
    
    #Allows you to ensure the Standard deviation remains the same through this process
    #c=y.std()
    #d=y2.std()
    #return c,d

    