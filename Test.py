import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


x = np.linspace(0, 1, 10)
y = pow(x,2)

plt.plot(x,y)
plt.show()

x2 = np.arange(0,1,0.01)
y2 = pow(x2,2)

plt.plot(x2,y2)
plt.show()