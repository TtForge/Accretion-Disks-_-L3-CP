from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
# from __FunctionBase import *
from Testing.__FunctionBase import *

steps = [101, 151, 201, 251, 301, 351, 401, 501, 601, 801, 1001, 1201, 1501, 2001]

# LumTotal1 = integrate_Varx(UnLogNuArr, LuminosityFnc, UnLogRArr)
# print(LumTotal1)

nuarray = UnLogNuArrVar(1001)
# print(UnLogNuArr)
# print(nuarray)
rarray = UnLogRArrVar(1001)
# print(UnLogRArr)
# print(rarray)

for i in range(len(UnLogRArr)):
    if rarray[i] == UnLogRArr[i]:
        print("True")
    else:
        print(rarray[i])
        print(UnLogRArr[i])
        print("False")

# LumTotal = integrate_Varx(UnLogNuArr, LuminosityFnc, UnLogRArr)
# print(LumTotal)
LumTotal2 = integrate_Varx(nuarray, LuminosityFnc, rarray)
print(LumTotal2)
