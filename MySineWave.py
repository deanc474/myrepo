import math
import matplotlib.pyplot as plt
import numpy as np

def MySineWave(w):
    
    x = np.linspace(-2*math.pi,2*math.pi,1000)
    y = np.sin(2*math.pi*x/w)
    
    plt.figure(1)
    a = plt.plot(x,y)
    return a