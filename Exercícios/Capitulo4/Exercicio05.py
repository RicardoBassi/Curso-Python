import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as sl
np.set_printoptions(suppress=True)

#1
print('parte 1')
x = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5])
y = np.array([-2.0, 0.5, -2.0, 1.0, -0.5, 1.0])

N = 6

V = np.vander(x, N)

print(V)

A = V[:,1:]

print(np.shape(A))
print(A)

#2
print('parte 2')
B = (sl.inv((A.T).dot(A))).dot(A.T)

print(np.shape(B))
print(B)

#3
print('parte 3')
c = B @ y

print(np.shape(c))
print(c)

print('parte 4')

f = np.polyval(c, x)

plt.plot(x,y,'*',label='data')
plt.plot(x,f,'r',label='fit')
plt.legend(loc=2, shadow=True)
plt.show()