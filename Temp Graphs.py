from cProfile import label
from distutils.log import Log
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math
import scipy.integrate as quad

# Constants    (FIND REFERENCES)
c = 299792458                               # metres per sec
G = 0.000000000066743                       # Neuton metres sqared per kg sqaured  
M_sol = 2000000000000000000000000000000     # Kg
SB = 0.0000005670374419                     # Stefan Boltzmann - Watt per square metre per Kelvin to forth
h = 6.62607015 * math.pow(10,-34)           # Joules per Hertz
k_B = 1.380649 * math.pow(10,-23)           # Boltzmann - Joules per Kelvin

# Galaxy Values
M = 10 * M_sol                              # Kg
Acc_rate = 1000000000000000                 # Kg per sec

R_g = (G * M) / c**2                        # metres
R_in = 6 * R_g                              # metres
R_out = 100000 * R_g                        # metres
r_in = 6
r_out = 100000

nu_st = math.pow(10, 14)
nu_end = math.pow(10, 19)

logR_in = np.log10(R_in)
LogR_out = np.log10(R_out)

lognu_st = np.log10(nu_st)
lognu_end = np.log10(nu_end)

# def Temp (R):   
#     numerator = G * M * Acc_rate
#     denominator = 8 * np.pi * math.pow(R,3) * SB
#     x = math.pow((numerator/denominator),1/4)
#     return x

def Temp (R):
    constant = (G * M * Acc_rate) / (8 * np.pi * SB)
    T4 = constant * 1/(pow(R,3))
    return pow(T4, 0.25)

def TempViscR (R):
    constant = (3 * G * M * Acc_rate)/(8 * np.pi * SB)
    T4 = constant * 1/(pow(R,3)) * (1 - pow((R_in/R), 0.5))
    return pow(T4, 0.25)
    
steps = 1000
# LogRArr = np.logspace(R_in,R_out, steps, True, 10)
LogRArr = np.linspace(np.log10(R_in),np.log10(R_out),steps)

TempArr = []
for i in range(0, len(LogRArr)):
    TempArr.append(Temp(10**LogRArr[i]))

TempViscArrR = []
for i in range(0, len(LogRArr)):
    TempViscArrR.append(TempViscR(10**LogRArr[i]))
TempViscArrR[0] = 0

plt.plot(LogRArr, TempArr, label = "Temp")
plt.plot(LogRArr, TempViscArrR, label = "Temp + Visc")
plt.legend()
plt.show()


# print((3 * G * M * Acc_rate)/(8 * np.pi * SB))
# print((((3 * G * M * Acc_rate)/(8 * np.pi * SB) * (1/((10**LogRArr[0])**3)) * (1-pow(R_in/(10**LogRArr[0]), 0.5))), 0.25))
# print(TempArr)
# print(TempViscArrR)





# def Flux (T, nu):
#     numerator = 2 * np.pi * h * math.pow(nu, 3) / math.pow(c, 2)
#     denominator = np.exp((h * nu)/(k_B * T) - 1)
#     x = np.pi * numerator/denominator
#     return x

# nu = 10000000000000000

# FluxArr = []
# for i in range(0, len(RArr)):
#     FluxArr.append(Flux(TempArr[i], nu))

# plt.plot(RArr, FluxArr, label = "Flux")
# plt.xscale('log')
# plt.legend()