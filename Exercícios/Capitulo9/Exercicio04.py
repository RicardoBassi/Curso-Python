from itertools import count, islice
import numpy as np


def s(n):
    return (1 + 1 / n)**(2*n)

# =============================================================================
# lista = []
# 
# k = 1000000
# 
# for i in np.arange(1,k,1):
#     lista.append(s(i))
#     if (abs( s(i) - np.exp(1)**2) >= 1e-5):
#         pass
#     else:
#         print(i)
#         break
#     
# =============================================================================
    
lista = []

def smallest_number(n):
    for i in np.arange(1,n,1):
        if (abs( s(i) - np.exp(1)**2) >= 1e-5):
            yield i
        else:
            print(i)
            break
        
result = smallest_number(1000000)
for k in result:
    pass