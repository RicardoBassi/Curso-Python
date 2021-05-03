import numpy as np

def polar_to_comp(r,phi):
    z = (r)*(np.exp(1j*phi))
    return z

print(polar_to_comp(2, 0))