from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import math
# from __FunctionBase import *
from Testing.__FunctionBase import *

plt.rcParams.update({
    "figure.facecolor":  (1.0, 1.0, 1.0, 0.0),  # red   with alpha = 30%
    "axes.facecolor":    (1.0, 1.0, 1.0, 0.0),  # green with alpha = 50%
    "savefig.facecolor": (1.0, 1.0, 1.0, 0.0),  # blue  with alpha = 20%
    "legend.framealpha": 0.2,
    "lines.linewidth":   3,
    "axes.linewidth":    3,
    "axes.labelsize":    20,
    "lines.markersize": 10,
    "xtick.labelsize": 16,
    "ytick.labelsize": 16,
    "legend.fontsize": 15,
    "axes.edgecolor": 'white',
    "xtick.labelcolor": 'white',
    "ytick.labelcolor": 'white',
    "axes.labelcolor": 'white',
    "legend.labelcolor": 'white',
    "text.color": 'white',
    "axes.spines.top":    False,
    "axes.spines.right":  False,
    "ytick.color": 'white',
    "legend.markerscale": 2,
    "font.family": 'serif',
    "mathtext.fontset": 'dejavuserif',
    "savefig.format": 'svg',
})

### Flux v Radius
for i in range(14, 20):
    plt.plot(LogR_to_Logr(LogRArr), np.log10(FluxArrViscFnc(UnLogRArr, math.pow(10,i))), label = "v = 10^" + str(i) + ' Hz')
plt.xlabel('Log(Radius / $R_g$)')
plt.ylabel('Log(Flux / $W m^{-2}$)')
plt.legend()
# plt.savefig('Graphs\LogLog Flux vs r.svg', format='svg')
plt.show()


### Flux v Temperature
for i in range (14, 20):
    plt.scatter(np.log10(TempViscArr[TMaxIndex:]), np.log10(FluxArrViscFnc(UnLogRArr, math.pow(10,i))[TMaxIndex:]), label = ("v = 10^" + str(i) + ' Hz'), marker = 'x', s=10,  linewidth=0.5)
    # plt.plot(TempViscArr, np.log10(FluxArray(TempViscArr, pow(10, i))), label = ("v = 10^" + str(i)))
plt.xlabel('Temperature / $K$')
plt.ylabel('Log(Flux / $W m^{-2}$)')
plt.legend()
plt.show()

for i in range (14, 20):
    plt.scatter(TempViscArr, FluxArrViscFnc(UnLogRArr, math.pow(10,i)), label = "v = 10^" + str(i) + ' Hz', marker = 'x', s=10, linewidth=0.5)
    # plt.plot(TempViscArr, FluxArray(TempViscArr, pow(10, i)), label = "v = 10^" + str(i))
plt.xlabel('Temperature / $K$')
plt.ylabel('Flux / $W m^{-2}$')
plt.legend()
plt.show()