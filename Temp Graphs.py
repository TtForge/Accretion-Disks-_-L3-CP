from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import math

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

#####################################################################

Rsteps = 1000
nusteps = 1000
print(Rsteps)
print(nusteps)
LogRArr = np.linspace(np.log10(R_in),np.log10(R_out), Rsteps)
LogNuArr = np.linspace(lognu_st, lognu_end, nusteps)

#####################################################################
### Temperature Functions ###########################################

def Temp (R):
    constant = (G * M * Acc_rate) / (8 * np.pi * SB)
    T4 = constant * 1/(pow(R,3))
    return pow(T4, 0.25)

def TempViscR (R):
    constant = (3 * G * M * Acc_rate)/(8 * np.pi * SB)
    T4 = constant * 1/(pow(R,3)) * (1 - pow((R_in/R), 0.5))
    return pow(T4, 0.25)
    
def TempArrFnc (fnc, R):
    arr = []
    for i in range(0,len(R)):
        arr.append(fnc(10**R[i]))
    return arr

TempArr = TempArrFnc(Temp, LogRArr)
TempViscArr = TempArrFnc(TempViscR, LogRArr)
TempViscArr[0] = 0.0000000000000001

print(TempArr)
print(TempViscArr)

#####################################################################
### Temperature Plotting ############################################

plt.plot(LogRArr, TempArr, label = "Temp")
plt.plot(LogRArr, TempViscArr, label = "Temp + Visc")
plt.xlabel('Log(Radius) / $m$')
plt.ylabel('Temperature / $K$')
plt.legend()
plt.show()

#####################################################################
### Flux Functions + Plotting #######################################

def Flux(T, nu):
    constant = (2 * np.pi * planck) / (c ** 2)
    exponent = (planck * nu) / (k_B * T)
    B_v = constant * pow(nu, 3) / (np.exp(exponent)-1)
    return np.pi * B_v

def FluxArray (Temp, v):
    FluxArr = []
    for i in range(0, len(Temp)):
        FluxArr.append(Flux(Temp[i], v))
    return FluxArr

for i in range (14, 20):
    plt.plot(LogRArr, FluxArray(TempViscArr, pow(10, i)), label = "v = 10^" + str(i))
plt.xlabel('Log(Radius) / $m$')
plt.ylabel('Flux / $J M^{-1}$')
plt.legend()
plt.show()

#####################################################################
### Integration and Luminosity Functions ############################

def integrate (x, y, nu):
    total = 0
    for i in range(0, len(x)-1):
        h = x[i+1] - x[i]
        total += h * (y(x[i], nu) + 4*y(x[i]+0.5*h, nu)+y(x[i]+h, nu))
    return 1/6 * total

def integrate2 (x, y, nu):
    total = 0
    steps = int(len(x) / 2)
    for i in range(0, steps-1):
        h = x[i+1] - x[i]
        total += h/3 * (y(x[2*i], nu) + 4 * y(x[2*i+1], nu) + y(x[2*i+2], nu))
    return total

def integrate_Lum (nu, Lum, LogR):
    total = 0
    for i in range(0, len(nu)-1):
        h = nu[i+1] - nu[i]
        total += h * (Lum(LogR, nu[i]) + 4* Lum(LogR, nu[i]+0.5*h) + Lum(LogR, nu[i] + h))
    return 1/6 * total

def integrate_Lum2 (nu, Lum, LogR):
    total = 0
    steps = int(len(nu) / 2)
    for i in range(0, steps-1):
        h = nu[i+1] - nu[i]
        total += h/3 * (Lum(LogR, nu[2*i]) + 4 * Lum(LogR, nu[2*i+1]) + Lum(LogR, nu[2*i+2]))
    return total

def integrand (R, nu):
    return Flux(TempViscR(R), nu) * 4 * np.pi * R

def Luminosity (R, nu):
    Lum = []
    for i in range(0, len(nu)):
        Lum.append(integrate2(np.power(10, R), integrand, nu[i]) * nu[i])
    return Lum

def LuminosityFnc (R, nu):
    return integrate2(np.power(10, R), integrand, nu)

#####################################################################
### Luminosity Total and Plotting ###################################

vLum_vals = Luminosity(LogRArr, np.power(10, LogNuArr))
plt.plot(LogNuArr, np.log10(vLum_vals))
plt.xlabel('$Log_{10}($\nu$)$ / $Hz$')
plt.ylabel('$Log_{10}(L)$ / $W$')
plt.show()

Lum_Tot = integrate_Lum(np.power(10, LogNuArr), LuminosityFnc, LogRArr)
print('Integrate 1 = ' + str(Lum_Tot))
Lum_Tot2 = integrate_Lum2(np.power(10, LogNuArr), LuminosityFnc, LogRArr)
print('Integrate 2 = ' + str(Lum_Tot))

#####################################################################