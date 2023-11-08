from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import math

#region Constants
#####################################################################

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

R_g = (G * M) / c**2 # ~14,852m               metres
R_in = 6 * R_g                              # metres
R_out = 100000 * R_g                        # metres

nu_st = math.pow(10, 14)
nu_end = math.pow(10, 19)
lognu_st = 14
lognu_end = 19

#endregion

#####################################################################

def MaxVal(y):
    i = np.argmax(y)
    return i+1

def unlog(x):
    return np.power(10, x)

#####################################################################

Rsteps = 1000
LogRArr = np.linspace(np.log10(R_in),np.log10(R_out), Rsteps)
UnlogRArr = unlog(LogRArr)
UnlogRArr[0] = R_in + 1
def LogRArrVar (steps):
    return np.linspace(np.log10(R_in),np.log10(R_out), steps)

nusteps = 1000
LogNuArr = np.linspace(lognu_st, lognu_end, nusteps)
UnLogNuArr = unlog(LogNuArr)
def LogNuArrVar (steps):
    return np.linspace(lognu_st, lognu_end, steps)

#region Temp fncs
#####################################################################
### Temperature Functions ###########################################

def Temp (R):
    constant = (G * M * Acc_rate) / (8 * np.pi * SB)
    T4 = constant * 1/(pow(R,3))
    return pow(T4, 0.25)

def TempViscR (R):
    constant = (3 * G * M * Acc_rate)/(8 * np.pi * SB)
    T4 = constant * (1/(pow(R, 3))) * (1 - np.power((R_in/R), 0.5))
    return np.power(T4, 0.25)
    
def TempArrFnc (fnc, R):
    arr = []
    for i in range(0,len(R)):
        arr.append(fnc(R[i]))
    return arr

def R_to_r (R):
    r = []
    for i in R:
        r.append(R[i]/R_g)
    return r

TempArr = TempArrFnc(Temp, UnlogRArr)
TempViscArr = TempArrFnc(TempViscR, UnlogRArr)
TempViscArr[0] = 0.0000000000000001

#endregion

#region Temp plotting
#####################################################################
### Temperature Plotting ############################################

plt.plot(LogRArr, TempArr, label = "Temp")
plt.plot(LogRArr, TempViscArr, label = "Temp + Visc")
plt.xlabel('Log(Radius / $m$)')
plt.ylabel('Temperature / $K$')
plt.legend()
plt.show()

#endregion

#region Flux fncs + plotting 
#####################################################################
### Flux Functions + Plotting #######################################

'''
def Flux(T, nu):
    constant = (2 * np.pi * planck) / (c ** 2)
    exponent = (planck * nu) / (k_B * T)
    B_v = (constant * pow(nu, 3)) / (np.exp(exponent) - 1)
    return np.pi * B_v
    
def FluxArray (T, nu):
    FluxArr = []
    for i in range(0, len(T)):
        FluxArr.append(Flux(T[i], nu))
    return FluxArr
'''

def Flux (Tfnc, nu, R):
    constant = (2 * np.pi * planck) / (c ** 2)
    exponent = (planck * nu) / (k_B * Tfnc(R))
    B_v = (constant * pow(nu, 3)) / (np.exp(exponent) - 1)
    return np.pi * B_v

def FluxVisc (R, nu):
    constant = (2 * np.pi * planck) / (c ** 2)
    exponent = (planck * nu) / (k_B * TempViscR(R))
    B_v = (constant * pow(nu, 3)) / (np.exp(exponent) - 1)
    return np.pi * B_v

def FluxArrayFnc (Tfnc, nu, RArr):
    FluxArr = []
    for i in range(0, len(RArr)):
        FluxArr.append(Flux(Tfnc, nu, RArr))
    return FluxArr

def FluxArrViscFnc (RArr, nu):
    FluxArr = []
    for i in range(0, len(RArr)):
        FluxArr.append(FluxVisc(RArr[i], nu))
    return FluxArr

print(np.power(10,14))

plt.plot(LogRArr, FluxArrViscFnc(UnlogRArr, 100000000000000000))

for i in range(14, 20):
    plt.plot(LogRArr, FluxArrViscFnc(UnlogRArr, 10**i), label = "v = 10^" + str(i) + ' Hz')
plt.xlabel('Log(Radius / $m$)')
plt.ylabel('Flux / $W m^{-2}$')
plt.legend()
plt.show()

#endregion
'''
#region Flux vs Temp Plotting
#####################################################################
### Flux vs Temp Plotting ###########################################

for i in range (14, 20):
    plt.scatter(TempViscArr, np.log10(FluxArray(TempViscArr, unlog(i))), label = ("v = 10^" + str(i) + ' Hz'), marker = 'x', s=10,  linewidth=0.5)
    # plt.plot(TempViscArr, np.log10(FluxArray(TempViscArr, pow(10, i))), label = ("v = 10^" + str(i)))
plt.xlabel('Temperature / $K$')
plt.ylabel('Log(Flux / $W m^{-2}$)')
plt.legend()
plt.show()

for i in range (14, 20):
    plt.scatter(TempViscArr, FluxArray(TempViscArr, unlog(i)), label = "v = 10^" + str(i) + ' Hz', marker = 'x', s=10, linewidth=0.5)
    # plt.plot(TempViscArr, FluxArray(TempViscArr, pow(10, i)), label = "v = 10^" + str(i))
plt.xlabel('Temperature / $K$')
plt.ylabel('Flux / $W m^{-2}$')
plt.legend()
plt.show()

#endregion

#region Integration and Luminosity Functions
#####################################################################
### Integration and Luminosity Functions ############################

def integrate_xVar (x, y, var):
    total = 0
    for i in range(0, len(x)-1):
        h = abs(x[i+1] - x[i])
        total += h/3 * (y(x[i], var) + 4*y(x[i]+0.5*h, var) + y(x[i+1], var))
    return total

def integrate_Varx (x, y, var):
    total = 0
    for i in range(0, len(x)-1):
        h = abs(x[i+1] - x[i])
        total += h/3 * (y(var, x[i]) + 4*y(var, x[i]+0.5*h) + y(var, x[i+1]))
    return total

def integrand (R, nu):
    return Flux(TempViscR(R), nu) * 4 * np.pi * R

def Luminosity (LogR, nu):
    Lum = []
    for i in range(0, len(nu)):
        Lum.append(integrate_xVar(unlog(LogR), integrand, nu[i]) * nu[i])
    return Lum

def LuminosityFnc (LogR, nu):
    return integrate_xVar(unlog(LogR), integrand, nu)

#endregion

#region Unused Function
#####################################################################
### Unused Functions ################################################

# def integrate2 (x, y, nu):
#     total = 0
#     steps = int(len(x) / 2)
#     for i in range(0, steps-1):
#         h = x[i+1] - x[i]
#         total += h/3 * (y(x[2*i], nu) + 4 * y(x[2*i+1], nu) + y(x[2*i+2], nu))
#     return total

# def integrate_Lum (nu, Lum, LogR):
#     total = 0
#     for i in range(0, len(nu)-1):
#         h = abs(nu[i+1] - nu[i])
#         total += h/3 * (Lum(LogR, nu[i]) + 4* Lum(LogR, nu[i]+0.5*h) + Lum(LogR, nu[i] + h))
#     return total

# def integrate_Lum2 (nu, Lum, LogR):
#     total = 0
#     steps = int(len(nu) / 2)
#     for i in range(0, steps-1):
#         h = nu[i+1] - nu[i]
#         total += h/3 * (Lum(LogR, nu[2*i]) + 4 * Lum(LogR, nu[2*i+1]) + Lum(LogR, nu[2*i+2]))
#     return total

#endregion

#region Integrand Plotting
#####################################################################
### Integrand Plotting ##############################################

for j in range(14,20):
    IntegrandArr = []
    for i in range(len(TempViscArr)):
        IntegrandArr.append(integrand(TempViscArr[i], unlog(j)))
    plt.plot(LogRArr, np.log10(IntegrandArr), label = 'v = 10^' + str(j) + ' Hz')
plt.xlabel('Log($Radius$ / $m$)')
plt.ylabel('Log($Flux$ / $W$)')
plt.show()

#endregion
'''
#region Luminosity Total and plotting
#####################################################################
### Luminosity Total and Plotting ###################################

j = MaxVal(TempViscArr)

# vLum_vals1 = Luminosity(LogRArr[:j], np.power(10, LogNuArr[:j]))
# plt.plot(LogNuArr[:j], np.log10(vLum_vals1))

'''
vLum_vals2 = Luminosity(LogRArr[j:], unlog(LogNuArr[j:]))
plt.plot(LogNuArr[j:], np.log10(vLum_vals2))
plt.xlabel('Log($\nu$ / $Hz$)')
plt.ylabel('Log($\nu$L / $W$)')
plt.show()

Lum_Tot = integrate_Varx(unlog(LogNuArr[j:]), LuminosityFnc, LogRArr[j:]) # integrate_Lum(np.power(10, LogNuArr[:j]), LuminosityFnc, LogRArr[:j]) +
print('Total Luminosity w/ 1000 steps = ' + str(Lum_Tot))
'''

# Lum_Tot2 = integrate_Lum2(np.power(10, LogNuArr[:j]), LuminosityFnc, LogRArr[:j]) + integrate_Lum2(np.power(10, LogNuArr[j:]), LuminosityFnc, LogRArr[j:])
# print('Integrate 2 = ' + str(Lum_Tot2))

"""
Lum_Log_Totals = []
Lum_Totals = []
steps = [100, 150, 200, 250, 300, 350, 400, 500, 600, 800, 1000, 1200, 1500, 2000]
for i in steps:
    LumTotal = integrate_Varx(unlog(LogNuArrVar(i)[j:]), LuminosityFnc, LogRArrVar(i)[j:])
    Lum_Totals.append(LumTotal)
    Lum_Log_Totals.append(np.log10(LumTotal)) # np.log10
plt.plot(steps, Lum_Totals)
plt.xlabel('Steps')
plt.ylabel('Total luminosity / $W$')
plt.show()
"""

# plt.plot(steps, Lum_Log_Totals)
# plt.xlabel('Steps')
# plt.ylabel('Log(Total luminosity / $W$)')
# plt.show()

#endregion

#####################################################################

# 07/11 22:19 Total Luminosity w/ 1000 steps = 8.849751105624847e+30