from cProfile import label
import matplotlib.pyplot as plt
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

plt.plot(LogR_to_Logr(LogRArr), TempArr, label = "Temp")
plt.plot(LogR_to_Logr(LogRArr), TempViscArr, label = "Temp + Visc")
plt.xlabel('Log(Radius / $R_g$)')
plt.ylabel('Temperature / $K$')
plt.legend()
# plt.savefig('Graphs\Temp vs logr.svg', format='svg')
plt.show()


#region Max temperature print
'''
print(UnLogRArr[MaxVal(TempViscArr)]/R_g)
print(TempViscArr[MaxVal(TempViscArr)])
'''
#endregion