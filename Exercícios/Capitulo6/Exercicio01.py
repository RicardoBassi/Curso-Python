import numpy as np
from matplotlib import pyplot as plt

# plot elipse

a = 3
b = 5
t = np.linspace(-50,50,500)


def y(t):
    y = a*np.cos(t)
    x = b*np.sin(t)
    return x, y

x, y = y(t)

plt.plot()
plt.plot(x, y, 'r')
plt.scatter(0, 0, color='blue')
plt.xlabel('x')
plt.ylabel('y')


plt.title('Plot de uma Elipse')

plt.grid()