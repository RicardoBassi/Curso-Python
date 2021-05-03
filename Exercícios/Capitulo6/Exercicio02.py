import numpy as np
from matplotlib import pyplot as plt


def mandelbrot(h,w, maxit=20):
    X,Y = np.meshgrid(np.linspace(-2, 0.8, w), np.linspace(-1.4, 1.4, h))
    c = X + Y*1j
    z = c
    exceeds = np.zeros(z.shape, dtype=bool)

    for iteration in range(maxit):
        z = z**2 + c
        exceeded = abs(z) > 4
        exceeds_now = exceeded & (np.logical_not(exceeds))
        exceeds[exceeds_now] = True
        z[exceeded] = 2 # limit the values to avoid overflow
    return exceeds

plt.imshow(mandelbrot(400,400),cmap='gray')
plt.axis('off')
