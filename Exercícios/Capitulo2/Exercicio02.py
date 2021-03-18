import numpy as np
from scipy import *
from matplotlib.pyplot import *


def f(n,x):
    return (np.cos(x) + 1j*np.sin(x) )**n

def g(n,x):
    return np.cos(n*x) + 1j*np.sin(n*x)

print(f(1,2)==g(1,2))

print(np.round(f(10,2),10) == np.round(g(10,2),10))


print(np.round(f(45,5.3),10) == np.round(g(45,5.3),10))