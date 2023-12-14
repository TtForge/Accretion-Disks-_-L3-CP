from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import math
from __FunctionBase import *
# from Testing.__FunctionBase import *
from __GraphDesign import *

plt.figure(figsize= (6.4,2.5))
for z, j in zip(range(14,19), range(2,len(colours))):
    IntegrandArr = []
    for i in range(len(UnLogRArr)):
        IntegrandArr.append(integrand(UnLogRArr[i], math.pow(10,z)))
    # plt.scatter(LogR_to_Logr(LogRArr), np.log10(IntegrandArr), label = FreqLabels[i], marker = 'x', s=10, linewidth=0.5, color=colours[-j])
    plt.plot(LogR_to_Logr(LogRArr), np.log10(IntegrandArr), label = FreqLabels[z], color=colours[-j])
plt.xlabel('Log$_{10}$(Radius / $R_g$)')
plt.ylabel('Log$_{10}$($\\frac{dL_{\\nu}}{dR}$ / $Wm$)')
plt.legend(bbox_to_anchor=(1,0.9))
plt.ylim(-3, 10)
plt.savefig('..\\Graphs\\_3-2 Log(Integrand) v Log(Radius) cropped.svg', format='svg')
plt.show()

for z, j in zip(range(14,20), range(2,len(colours))):
    IntegrandArr = []
    for i in range(len(UnLogRArr)):
        IntegrandArr.append(integrand(UnLogRArr[i], math.pow(10,z)))
    # plt.scatter(LogR_to_Logr(LogRArr), np.log10(IntegrandArr), label = FreqLabels[i], marker = 'x', s=10, linewidth=0.5, color=colours[-j])
    plt.plot(LogR_to_Logr(LogRArr), np.log10(IntegrandArr), label = FreqLabels[z], color=colours[-j])
plt.xlabel('Log$_{10}$(Radius / $R_g$)')
plt.ylabel('Log$_{10}$($\\frac{dL_{\\nu}}{dR}$ / $Wm$)')
plt.legend(loc = 'lower left', prop={'size': 10}) # bbox_to_anchor=(1,0.7))
plt.savefig('..\\Graphs\\_3-1 Log(Integrand) v Log(Radius) full.svg', format='svg')
plt.show()