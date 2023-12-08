from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import math
# from __FunctionBase import *
from Working.__FunctionBase import *

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

plt.figure(figsize= (6.4,2.5))
for z in range(14,20):
    IntegrandArr = []
    for i in range(len(UnLogRArr)):
        IntegrandArr.append(integrand(UnLogRArr[i], math.pow(10,z)))
    plt.scatter(LogR_to_Logr(LogRArr), np.log10(IntegrandArr), label = 'v = 10^' + str(z) + ' Hz', marker = 'x', s=10, linewidth=0.5)
plt.xlabel('Log($Radius$ / $R_g$)')
plt.ylabel('Log($d(L_{\\nu})/dR$ / $Wm$)')
plt.legend(bbox_to_anchor=(1,0.7))
plt.ylim(-3, 10)
# plt.savefig('Graphs\LogLog cropped Integrand vs r.svg', format='svg')
plt.show()

for z in range(14,20):
    IntegrandArr = []
    for i in range(len(UnLogRArr)):
        IntegrandArr.append(integrand(UnLogRArr[i], math.pow(10,z)))
    plt.scatter(LogR_to_Logr(LogRArr), np.log10(IntegrandArr), label = 'v = 10^' + str(z) + ' Hz', marker = 'x', s=10, linewidth=0.5)
plt.xlabel('Log($Radius$ / $R_g$)')
plt.ylabel('Log($d(L_{\\nu})/dR$ / $Wm$)')
plt.legend(loc = 'lower left', prop={'size': 10}) # bbox_to_anchor=(1,0.7))
# plt.savefig('Graphs\LogLog Integrand vs r.svg', format='svg')
plt.show()