import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

def Resampling(x,y,xnew): #Note: xnew, is the new x vector.
    
    #First Calculate the Sampling frequency 
    #nu = mx + b
    
    #initial axis
    mi,bi = SamplingFrequencies(x)
    
    #final axis
    mf,bf = SamplingFrequencies(xnew)
    
    deltam = mf/mi #This is the factor by which the distance between data points must expand or contract
    deltab = bf-bi #this is the distance the data points must be translated
    step = x[1]-x[0]
    shift = -1*deltab/step
    
    if deltam > 1: #zero pad
        dm = int(round(deltam))
        rem = deltam-dm
        X,Y = FTExp(x,y,dm)
        
        #Then use trigonometric Interpolation to move the remaining factor
        X,Y = TrigInterp(X,Y,(1+rem)*len(X)) 
        
        #Lastly Shift the data
        X,Y = FFTShift(X,Y,shift)
        
    elif deltam < 1: #DownSample
        dm = int(round(deltam))
        rem = deltam-dm
        if len(x) % 2 == 0: # If the len(x) is even
            if dm % 2 == 0:#and dm is even (We CAN DownSample)
                X,Y = FTCont(x,y,dm*len(x)) 
                
                #Then use trigonometric Interpolation to move the remaining factor
                X,Y = TrigInterp(X,Y,(1+rem)*len(X))
                
                #Lastly Shift the data
                X,Y = FFTShift(X,Y,shift)
            else: #We Cannot Downsample
                #We must use trigonometric Interpolation
                X,Y = TrigInterp(X,Y,deltam*len(X))
                
                #Lastly Shift the data
                X,Y = FFTShift(X,Y,shift)
        else: # If the len(x) is odd
            if dm % 2 == 1:#and dm is odd (We CAN DownSample)
                X,Y = FTCont(x,y,dm*len(x)) 
                
                #Then use trigonometric Interpolation to move the remaining factor
                X,Y = TrigInterp(X,Y,(1+rem)*len(X))
                
                #Lastly Shift the data
                X,Y = FFTShift(X,Y,shift)
            else: #We Cannot Downsample
                #We must use trigonometric Interpolation
                X,Y = TrigInterp(X,Y,deltam*len(X))
                
                #Lastly Shift the data
                X,Y = FFTShift(X,Y,shift)
        return X,Y
    