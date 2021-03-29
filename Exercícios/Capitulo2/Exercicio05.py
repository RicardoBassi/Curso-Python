import numpy as np
from scipy import *
from matplotlib.pyplot import *


def implication(A,B):
    if A == False or (A and B):
        return True

    else:
        return False
    
print("C is {0}".format(implication(False, True)))

print("C is {0}".format(implication(False, False)))

print("C is {0}".format(implication(True, True)))

print("C is {0}".format(implication(True, False)))