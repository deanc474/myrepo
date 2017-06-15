import numpy as np


def SamplingFrequencies(nu):
    m,b = np.polyfit(np.arange(len(nu)), nu, 1)
    return m, b