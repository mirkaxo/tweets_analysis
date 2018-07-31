import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

x = [-3 ,-2,-1, -0.5, 1, 2, 3, 4]
num_bins = 20
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.show()
