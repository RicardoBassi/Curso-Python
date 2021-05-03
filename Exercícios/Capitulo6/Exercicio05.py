from matplotlib import pyplot as plt
import numpy as np
import imageio
from scipy.ndimage import gaussian_laplace

im = imageio.imread('imageio:coffee.png')


plt.figure(figsize = (10,10))
plt.subplot(121)
plt.axis(False)
plt.imshow(im)

im_gray = np.mean(im, axis = 2)
plt.gray()
mod = gaussian_laplace(im_gray, sigma=5)

plt.subplot(122)
plt.axis(False)
plt.imshow(mod)