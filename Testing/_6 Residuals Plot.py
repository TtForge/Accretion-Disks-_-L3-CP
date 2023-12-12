from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
from __FunctionBase import *
# from Testing.__FunctionBase import *
from __GraphDesign import *

NuArr1001 = UnLogNuArrVar(1001)
RArr1001 = UnLogRArrVar(1001)

ReferenceLum = Luminosity(RArr1001, NuArr1001)
ReferenceLumTot = integrate_Varx2(NuArr1001, LuminosityFnc2, RArr1001)

R_steps = [251, 301, 351, 401, 501, 601, 801]  # 101, 151, 201,  1201, 1501, 2001
R_steps2 = [2001, 2501, 3001, 3501, 4001]
Nu_steps = [151, 201, 251, 301, 351, 401, 501, 601, 801, 1001, 1201, 1501, 2001, 2501, 3001]

def RVariance(StepVal, LumFnc, j, mode):
    for i, k in zip(StepVal, range(2,len(colours))):
        NuArr = UnLogNuArrVar(1001)
        RArr = UnLogRArrVar(i)
        vLum_vals2 = np.array(LumFnc(RArr, NuArr)) / np.array(ReferenceLum)
        plt.plot(np.log10(NuArr), vLum_vals2, label='$Bins_{R} = $' + str(i), color = colours[-k])
    plt.xlabel('Log($\\nu$ / $Hz$)')
    plt.ylabel('Residuals $\\frac{L_{\\nu}}{L_{\\nu, ref}}$')
    plt.title('Luminosity residuals varyied w/ radial bins, reference of 1001 bins. Method ' + str(j))
    plt.savefig('..\\Graphs\\_6-1-' + str(j) + ' Radial bin residuals v Frequency ' + mode + '.svg', format='svg')
    plt.legend(bbox_to_anchor=(1,0.7))
    plt.show()

RVariance(R_steps, Luminosity, 1, 'Lower')
RVariance(R_steps2, Luminosity, 1, 'Higher')

RVariance(R_steps, Luminosity2, 2, 'Lower')
RVariance(R_steps2, Luminosity2, 2, 'Higher')

def NuVariance(IntFnc, j):
    LumBins = []
    for i in Nu_steps:
        NuArr = UnLogNuArrVar(i)
        RArr = UnLogRArrVar(1001)
        LumBins.append(IntFnc(NuArr, LuminosityFnc2, RArr) / ReferenceLumTot)
    plt.plot(Nu_steps, LumBins, color = colours[4])
    plt.xlabel('Frequency Bins')
    plt.ylabel('Residuals $\\frac{L_{total}}{L_{total, ref}}$')
    plt.title('Total luminosity residuals varied w/ frequency bins, reference of 1001 bins. Method ' + str(j))
    plt.savefig('..\\Graphs\\_6-2-' + str(j) + ' Frequency bin residuals v steps.svg', format='svg')
    plt.legend(bbox_to_anchor=(1,0.7))
    plt.show()
    
NuVariance(integrate_Varx, 1)
NuVariance(integrate_Varx2, 2)