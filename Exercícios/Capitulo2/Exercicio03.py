import numpy as np
from scipy import *
from matplotlib.pyplot import *


def f(x):
    return np.exp(1j*x)

def g(x):
    return np.cos(x) + 1j*np.sin(x)

print(f(2)==g(2))

print(np.round(f(2),10) == np.round(g(2),10))


print(np.round(f(5.3),10) == np.round(g(5.3),10))