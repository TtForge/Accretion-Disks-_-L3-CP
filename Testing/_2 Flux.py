from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import math
from __FunctionBase import *
# from Testing.__FunctionBase import *
from __GraphDesign import *

### Flux v Radius
for i, j in zip(range(14, 20), range(2,len(colours))):
    plt.plot(LogR_to_Logr(LogRArr), np.log10(FluxArrViscFnc(UnLogRArr, math.pow(10,i))), label = FreqLabels[i], color=colours[-j])
plt.xlabel('Log$_{10}$(Radius / $R_g$)')
plt.ylabel('Log$_{10}$(Flux / $W m^{-2}$)')
plt.legend()
plt.savefig('..\\Graphs\\_2-1 Log(Flux) v Log(r).svg', format='svg')
plt.show()


### Flux v Temperature
for i, j in zip(range(14, 20), range(2,len(colours))):
    # plt.scatter(np.log10(TempViscArr[TMaxIndex:]), np.log10(FluxArrViscFnc(UnLogRArr, math.pow(10,i))[TMaxIndex:]), label = ("v = 10^" + str(i) + ' Hz'), marker = 'x', s=10,  linewidth=0.5, color=colours[-j])
    plt.plot(np.log10(TempViscArr[TMaxIndex:]), np.log10(FluxArrViscFnc(UnLogRArr, math.pow(10,i))[TMaxIndex:]), label = FreqLabels[i], color=colours[-j])
plt.xlabel('Temperature / $K$')
plt.ylabel('Log$_{10}$(Flux / $W m^{-2}$)')
plt.legend(loc = 4)
plt.savefig('..\\Graphs\\_2-2 Log(Flux) v Log(Temperature).svg', format='svg')
plt.show()

for i, j in zip(range(14, 20), range(2,len(colours))):
    # plt.scatter(TempViscArr, FluxArrViscFnc(UnLogRArr, math.pow(10,i)), label = "v = 10^" + str(i) + ' Hz', marker = 'x', s=10, linewidth=0.5, color=colours[-j])
    plt.plot(TempViscArr[TMaxIndex:], FluxArrViscFnc(UnLogRArr, math.pow(10,i))[TMaxIndex:], label = FreqLabels[i], color=colours[-j])
plt.xlabel('Temperature / $K$')
plt.ylabel('Flux / $W m^{-2}$')
plt.legend()
plt.savefig('..\\Graphs\\_2-3 Log(Flux) v Temperature.svg', format='svg')
plt.show()