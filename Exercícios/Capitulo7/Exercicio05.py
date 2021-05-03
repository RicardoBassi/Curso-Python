import numpy as np

def maxdivisor(a,b):
    return np.gcd(a,b)

def mindivisor(a,b):
    return ((abs(a*b)) / maxdivisor(a,b))