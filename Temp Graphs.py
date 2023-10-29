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

nu_st = math.pow(10, 14)
nu_end = math.pow(10, 19)

logR_in = np.log10(R_in)
LogR_out = np.log10(R_out)

lognu_st = np.log10(nu_st)
lognu_end = np.log10(nu_end)

def Temp (R):   
    numerator = G * M * Acc_rate
    denominator = 8 * np.pi * math.pow(R,3) * SB
    x = math.pow((numerator/denominator),1/4)
    return x

steps = 1000
LogRArr = np.linspace(logR_in,LogR_out, steps)
RArr = np.linspace(R_in,R_out,steps)

LogTempArr = []
for i in range(0, len(LogRArr)):
    LogTempArr.append(Temp(LogRArr[i]))
    
TempArr = []
for i in range(0, len(RArr)):
    TempArr.append(Temp(RArr[i]))
    
plt.loglog(RArr,TempArr)