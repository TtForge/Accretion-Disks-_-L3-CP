from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
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

### Plot
vLum_vals2 = LuminosityNu(UnLogRArr, UnLogNuArr)
plt.plot(LogNuArr, np.log10(vLum_vals2))
plt.xlabel('Log($\\nu$ / $Hz$)')
plt.ylabel('Log($\\nu L_{\\nu}$ / $W Hz$)')
# plt.savefig('Graphs\LogLog nuL vs nu.svg', format='svg')
plt.show()


NuArr = UnLogNuArrVar(5001)
RArr = UnLogRArrVar(1001)

### Total
Lum_Tot = integrate_Varx2(NuArr, LuminosityFnc2, RArr) # integrate_Lum(np.power(10, LogNuArr[:TMaxIndex]), LuminosityFnc, LogRArr[:TMaxIndex]) +
print('Total Luminosity int2 w/ 1000 nu & R steps = ' + str(Lum_Tot)) 
# RSteps = 1001, NuSteps = 5001, L_tot = 7.488502463784719e+30



Lum_Tot2 = integrate_Varx(NuArr, LuminosityFnc, RArr) # integrate_Lum(np.power(10, LogNuArr[:TMaxIndex]), LuminosityFnc, LogRArr[:TMaxIndex]) +
print('Total Luminosity int1 w/ 1000 nu & R steps = ' + str(Lum_Tot2)) 
# RSteps = 1001, NuSteps = 5001, L_tot = 7.488254168200538e+30