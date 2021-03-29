import numpy as np

#f(x) = x**2 + 0.25*x - 5

#bhaskara

a = 1
b = 0.25
c = -5

delta = b**2 -4*a*c

raizp = (-b + np.sqrt(delta))/2*a

raizn = (-b - np.sqrt(delta))/2*a

print("a raíz positiva é {0}".format(raizp))

print("a raíz negativa é {0}".format(raizn))