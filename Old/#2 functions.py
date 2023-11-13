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
planck = 6.62607015 * math.pow(10,-34)           # Joules per Hertz
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

def Flux (T, nu):
    numerator = 2 * np.pi * h * math.pow(nu, 3) / math.pow(c, 2)
    denominator = np.exp((h * nu)/(k_B * T) - 1)
    x = np.pi * numerator/denominator
    return x

steps = 100
# RLogArr = np.logspace(R_in, R_out, steps, True, 10)
# NuLogArr = np.logspace(nu_st, nu_end, steps, True, 10)
# h = (np.log10(R_in)-np.log10(R_out))/steps
RLogArr = np.linspace(logR_in, LogR_out, steps)
NuLogArr = np.linspace(lognu_st, lognu_end, steps)
h = (logR_in-LogR_out)/steps

print(RLogArr)

def Luminosity (nu):
    IntegArr = []
    for i in range(0, len(RLogArr)):
        IntegArr.append(Flux(Temp(RLogArr[i]),nu)*4*np.pi*RLogArr[i])
    total = 0
    for j in range(0, len(IntegArr)):
        total += IntegArr[j]
    return (h/2)*(IntegArr[0]+IntegArr[-1])+h*total

LumArr = []
for i in range(0,len(NuLogArr)):
    LumArr.append(Luminosity(NuLogArr[i]))


# plt.plot(NuLogArr, LumArr)


    

    
        
    
        


