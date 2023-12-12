from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
from __FunctionBase import *
# from Testing.__FunctionBase import *
from __GraphDesign import *

'''
### Plot
vLum_vals2 = LuminosityNu(UnLogRArr, UnLogNuArr)
plt.plot(LogNuArr, np.log10(vLum_vals2), color=colours[4])
plt.xlabel('Log($\\nu$ / $Hz$)')
plt.ylabel('Log($\\nu L_{\\nu}$ / $W Hz$)')
plt.savefig('..\\Graphs\\_4 Log(nu x Luminosity) v Log(nu).svg', format='svg')
plt.show()
'''

NuArr = UnLogNuArrVar(5001)
RArr = UnLogRArrVar(1001)

### Total
Lum_Tot = integrate_Varx2(NuArr, LuminosityFnc2, RArr) # integrate_Lum(np.power(10, LogNuArr[:TMaxIndex]), LuminosityFnc, LogRArr[:TMaxIndex]) +
print('Total Luminosity int2 w/ 1000 nu & R steps = ' + str(Lum_Tot)) 
# RSteps = 1001, NuSteps = 5001, L_tot = 7.488502463784719e+30



Lum_Tot2 = integrate_Varx(NuArr, LuminosityFnc, RArr) # integrate_Lum(np.power(10, LogNuArr[:TMaxIndex]), LuminosityFnc, LogRArr[:TMaxIndex]) +
print('Total Luminosity int1 w/ 1000 nu & R steps = ' + str(Lum_Tot2)) 
# RSteps = 1001, NuSteps = 5001, L_tot = 7.488254168200538e+30