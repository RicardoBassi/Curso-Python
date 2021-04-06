import numpy as np

v = np.array([[1,-1,1]], dtype=float)

print('shape {0}'.format(np.shape(v.T)))



P = v.dot(v.T) / (v.T).dot(v)

I = np.identity(3)

Q = I - P



print('Para P:')

print(P.dot(v.T))

print(v.T)

print('v.T é autovetor de P com autovalor 9')



print('Para Q:')

print(Q.dot(v.T))

print(v.T)

print('v.T é autovetor de P com autovalor -8')