from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
from __FunctionBase import *
# from Testing.__FunctionBase import *
from __GraphDesign import *

### Varying Bins

steps = [101, 151, 201, 251, 301, 351, 401, 501, 601, 801, 1001, 1201, 1501, 2001] #2501, 3501, 4001, 4501, 5001]


Lum_Log_Totals = []
Lum_Totals = []
for i in steps:
    NuArr = UnLogNuArrVar(i)
    RArr = UnLogRArrVar(i)
    LumTotal = integrate_Varx2(NuArr, LuminosityFnc2, RArr)
    Lum_Totals.append(LumTotal)
    Lum_Log_Totals.append(np.log10(LumTotal))
    
plt.plot(steps, Lum_Totals)
plt.xlabel('Steps')
plt.ylabel('Total luminosity / $W$')
plt.show()

    
NuArr = 0
RArr = 0

for i in steps:
    RStepsVary = []
    for j in steps:
        NuArr = UnLogNuArrVar(i)
        RArr = UnLogRArrVar(j)
        RVariance = integrate_Varx2(NuArr, LuminosityFnc2, RArr)
        RStepsVary.append(RVariance)
    plt.plot(steps, RStepsVary, label =('Nu Steps ' + str(i)))
plt.xlabel('Radial Steps')
plt.ylabel('Total luminosity / $W$')
plt.legend()
plt.show()

######## DO VARYING BINS WITH DIFFERENCE TO SOME VALUE


# plt.plot(steps, Lum_Log_Totals)
# plt.xlabel('Steps')
# plt.ylabel('Log(Total luminosity / $W$)')
# plt.show()
