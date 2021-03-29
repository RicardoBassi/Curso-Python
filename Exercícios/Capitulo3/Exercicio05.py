import numpy as np
from matplotlib import pyplot as plt

h = (1/1000)
a = (-0.5)

u = [np.exp(0),np.exp(h*a),np.exp(2*h*a)]

for i in np.arange(0,997,1):
    x = u[i+2] + h*a*((23/12)*u[i+2] - (4/3)*u[i+1] + (5/12)*u[i])
    u.append(x)


td = []

for j in np.arange(0,1000,1):
    y = j*h
    td.append(y)
    

plt.title('Plot 1')
plt.plot(u,td,'r',linewidth=1.0,label='')
plt.show()


plt.title('Plot 1')
plt.plot(u,td,'r',linewidth=1.0,label='')
plt.show()

ab = []

for k in np.arange(0,1000,1):
    z = abs(np.exp(a*td[k]) - u[k])
    ab.append(z)

plt.title('Plot 2')
plt.plot(td,ab,'r',linewidth=1.0,label='')
plt.ylabel("diferença")
plt.xlabel("n*h")
plt.show()