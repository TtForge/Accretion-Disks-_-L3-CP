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

NuArr1001 = UnLogNuArrVar(1001)
RArr1001 = UnLogRArrVar(1001)

ReferenceLum = Luminosity(RArr1001, NuArr1001)
ReferenceLumTot = integrate_Varx2(NuArr1001, LuminosityFnc2, RArr1001)

R_steps = [251, 301, 351, 401, 501, 601, 801]  # 101, 151, 201,  1201, 1501, 2001
R_steps2 = [2001, 2501, 3001, 3501, 4001]
Nu_steps = [151, 201, 251, 301, 351, 401, 501, 601, 801, 1001, 1201, 1501, 2001, 2501, 3001]

for i in R_steps:
    NuArr = UnLogNuArrVar(1001)
    RArr = UnLogRArrVar(i)
    vLum_vals2 = np.array(Luminosity(RArr, NuArr)) / np.array(ReferenceLum)
    plt.plot(np.log10(NuArr), vLum_vals2, label='Radial Bins ' + str(i))
plt.xlabel('Log($\\nu$ / $Hz$)')
plt.ylabel('Residuals $\\frac{L_{\\nu}}{L_{\\nu, ref}}$')
plt.title('Residuals plot for varying radial bins, reference value of 1001 bins (Radial/Freq.)')
# plt.savefig('Graphs\LogLog nuL vs nu.svg', format='svg')
plt.legend(bbox_to_anchor=(1,0.7))
plt.show()

for i in R_steps2:
    NuArr = UnLogNuArrVar(1001)
    RArr = UnLogRArrVar(i)
    vLum_vals2 = np.array(Luminosity(RArr, NuArr)) / np.array(ReferenceLum)
    plt.plot(np.log10(NuArr), vLum_vals2, label='Radial Bins ' + str(i))
plt.xlabel('Log($\\nu$ / $Hz$)')
plt.ylabel('Residuals $\\frac{L_{\\nu}}{L_{\\nu, ref}}$')
plt.title('Residuals plot for varying radial bins, reference value of 1001 bins (Radial/Freq.)')
# plt.savefig('Graphs\LogLog nuL vs nu.svg', format='svg')
plt.legend(bbox_to_anchor=(1,0.7))
plt.show()

LumBins = []
for i in Nu_steps:
    NuArr = UnLogNuArrVar(i)
    RArr = UnLogRArrVar(1001)
    LumBins.append(integrate_Varx2(NuArr, LuminosityFnc2, RArr) / ReferenceLumTot)
plt.plot(Nu_steps, LumBins)
plt.xlabel('Steps')
plt.ylabel('Residuals $\\frac{L_{total}}{L_{total, ref}}$')
plt.title('Total luminosity residuals plot for varying frequency bins, reference value of 1001 bins (Radial/Freq.)')
# plt.savefig('Graphs\LogLog nuL vs nu.svg', format='svg')
plt.show()