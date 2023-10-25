import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math

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

# list = [M, Acc_rate, R_g, R_in, R_out]

# for i in range(0,4):
#     print(list[i])
#     print(len(str(list[i])))
 
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

R_steps = 1000
nu_steps = 100

R_range = np.linspace(R_in, R_out, R_steps)
nu_range = np.linspace(nu_st, nu_end, nu_steps)

array_R_nu = []

for i in range(0, len(nu_range)):
    R_list = []
    for j in range(0, len(R_range)):
        R_list.append(Flux(Temp(R_range[j]), nu_range[i]))
    array_R_nu.append(R_list)

        
        



