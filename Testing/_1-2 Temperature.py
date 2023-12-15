from cProfile import label
import matplotlib.pyplot as plt
from __FunctionBase import *
# from Testing.__FunctionBase import *
from __GraphDesign import *

'''
plt.plot(LogR_to_Logr(LogRArr), TempArr, '--', label = "Temp", color=colours[1])
plt.plot(LogR_to_Logr(LogRArr), TempViscArr, label = "Temp + Visc", color=colours[4])
plt.xlabel('Log$_{10}$(Radius / $R_g$)')
plt.ylabel('Temperature / $K$')
plt.legend(bbox_to_anchor=(0.9,0.8), fontsize = 18)
plt.savefig('..\\Graphs\\_1 Temperature v Log(r).svg', format='svg')
plt.show()
'''

#region Max temperature print

print(TempViscArr[MaxVal(TempViscArr)])
print(UnLogRArr[MaxVal(TempViscArr)]/R_g)
print(UnLogRArr[MaxVal(TempViscArr)])

#endregion