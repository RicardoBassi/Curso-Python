import numpy as np
from scipy import *
from matplotlib.pyplot import *


u = 1.0 # you have to use a float here!
uold = 10.0

for iteration in range(2000):
    if abs(u-uold) < 1.e-8:
        print('Convergence')
        break # sequence has converged
    uold = u
    u = 2*u
else:
    print('No convergence')