from cProfile import label
from distutils.log import Log
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math
import scipy as sci

x = np.linspace(1,17,17)

# (y[0] + y[-1] + 4 * sum(y[1:-2:2]) + 2 * sum(y[2:-3:2]) + y[i+1])

print(x[0])
print(x[-1])
print(x[1:-1:2])
print(x[2:-1:2])