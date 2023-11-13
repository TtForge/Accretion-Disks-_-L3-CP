from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import math
from Testing.FunctionBase import *

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

#####################################################################

#region Max temperature print
'''
print(UnLogRArr[MaxVal(TempViscArr)]/R_g)
print(TempViscArr[MaxVal(TempViscArr)])
'''
#endregion

#####################################################################

#region Temperature plotting

plt.plot(LogR_to_Logr(LogRArr), TempArr, label = "Temp")
plt.plot(LogR_to_Logr(LogRArr), TempViscArr, label = "Temp + Visc")
plt.xlabel('Log(Radius / $R_g$)')
plt.ylabel('Temperature / $K$')
plt.legend()
# plt.savefig('Graphs\Temp vs logr.svg', format='svg')
plt.show()

#endregion

#####################################################################

#region Flux plotting

'''
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
'''

#endregion

#####################################################################

#region Integrand Plotting

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

# endregion

#####################################################################

# region Luminosity Total and plotting

vLum_vals2 = Luminosity(UnLogRArr[TMaxIndex:], UnLogNuArr[TMaxIndex:])
plt.plot(LogNuArr[TMaxIndex:], np.log10(vLum_vals2))
plt.xlabel('Log($\\nu$ / $Hz$)')
plt.ylabel('Log($\\nu L_{\\nu}$ / $W Hz$)')
plt.savefig('Graphs\LogLog nuL vs nu.svg', format='svg')
plt.show()

Lum_Tot = integrate_Varx2(UnLogNuArr, LuminosityFnc2, UnLogRArr) # integrate_Lum(np.power(10, LogNuArr[:TMaxIndex]), LuminosityFnc, LogRArr[:TMaxIndex]) +
print('Total Luminosity w/ 1000 nu & R steps = ' + str(Lum_Tot)) 

# endregion

#####################################################################
'''
# region Varying bins plots

Lum_Log_Totals = []
Lum_Totals = []
steps = [100, 150, 200, 250, 300, 350, 400, 500, 600, 800, 1000, 1200, 1500, 2000]
for i in steps:
    LumTotal = integrate_Varx(unlog(LogNuArrVar(i)[TMaxIndex:]), LuminosityFnc, LogRArrVar(i)[TMaxIndex:])
    Lum_Totals.append(LumTotal)
    Lum_Log_Totals.append(np.log10(LumTotal)) # np.log10
plt.plot(steps, Lum_Totals)
plt.xlabel('Steps')
plt.ylabel('Total luminosity / $W$')
plt.show()

plt.plot(steps, Lum_Log_Totals)
plt.xlabel('Steps')
plt.ylabel('Log(Total luminosity / $W$)')
plt.show()

#endregion
'''