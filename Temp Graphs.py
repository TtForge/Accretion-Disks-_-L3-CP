from cProfile import label
from distutils.log import Log
from random import lognormvariate
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math
import scipy as sci

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
r_in = 6
r_out = 100000

nu_st = math.pow(10, 14)
nu_end = math.pow(10, 19)

#################

def Temp (R):
    constant = (G * M * Acc_rate) / (8 * np.pi * SB)
    T4 = constant * 1/(pow(R,3))
    return pow(T4, 0.25)

def TempViscR (R):
    constant = (3 * G * M * Acc_rate)/(8 * np.pi * SB)
    T4 = constant * 1/(pow(R,3)) * (1 - pow((R_in/R), 0.5))
    return pow(T4, 0.25)
    
Rsteps = 1000
# LogRArr = np.logspace(R_in,R_out, Rsteps, True, 10)
LogRArr = np.linspace(np.log10(R_in),np.log10(R_out), Rsteps)
nusteps = 1000
LogNuArr = np.linspace(np.log10(nu_st), np.log10(nu_end), nusteps)


TempArr = []
for i in range(0, len(LogRArr)):
    TempArr.append(Temp(10**LogRArr[i]))

TempViscArr = []
for i in range(0, len(LogRArr)):
    TempViscArr.append(TempViscR(10**LogRArr[i]))
TempViscArr[0] = 0.0000000000000001

plt.plot(LogRArr, TempArr, label = "Temp")
plt.plot(LogRArr, TempViscArr, label = "Temp + Visc")
plt.xlabel('Log(Radius) / $m$')
plt.ylabel('Temperature / $K$')
plt.legend()
plt.show()

def Flux(T, nu):
    constant = (2 * np.pi * planck) / (c ** 2)
    exponent = (planck * nu) / (k_B * T)
    B_v = constant * pow(nu, 3) / (np.exp(exponent)-1)
    return np.pi * B_v

# nu_power = 14
# nu = pow(10, nu_power)

def FluxArray (Temp, v):
    FluxArr = []
    for i in range(0, len(Temp)):
        FluxArr.append(Flux(Temp[i], v))
    return FluxArr


#### 10**(LogNuArr[-1])
for i in range (14, 20):
    plt.plot(LogRArr, FluxArray(TempViscArr, pow(10, LogNuArr[i])), label = "v = 10^" + str(i))
plt.xlabel('Log(Radius) / $m$')
plt.ylabel('Flux / $J M^{-1}$')
plt.legend()
plt.show()
    
def integrate (x, y):
    h = x[1] - x[0]
    return h/3 * (y[0] + y[-1] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-1:2]))

def integrate2 (x, y, nu):
    total = 0
    for i in range(0, len(x)-1):
        h = x[i+1] - x[i]
        total += h * (y(x[i], nu) + 4*y(x[i]+0.5*h, nu)+y(x[i]+h, nu))
    return 1/6 * total

def integrand(R, nu):
    return Flux(Temp(R), nu) * 4 * np.pi * R

def Luminosity2 (R, nu):
    Lum = []
    for i in range(0, len(nu)):
        Lum.append(integrate2(np.power(10, R), integrand, nu[i]))
    return Lum

def Luminosity3 (R, nu):
    Lum = []
    for i in range(0, len(nu)):
        Lum.append(integrate2(np.power(10, R), integrand, nu[i]) * nu[i])
    return Lum
    
def Luminosity1 (Flux, R, nu):
    integrand = []
    for i in range(0, len(Flux)):
        integrand.append(Flux[i] * 4 * np.pi * R[i])
    return integrate(TempViscArr, integrand)

LumArr = []
for i in range(0,len(LogNuArr)):
    LumArr.append(Luminosity1(FluxArray(TempViscArr, 10**LogNuArr[i]), np.power(10,LogRArr), 10**(LogNuArr[i])))
    
print(LumArr)
    
plt.plot(LogNuArr, np.log10(LumArr), label = "Luminsoity")
plt.xlabel('$Log_{10}($\nu$)$ / $Hz$')
plt.ylabel('Luminosity / $W$')
plt.show()

print(Luminosity2(LogRArr, np.power(10, LogNuArr)))

plt.plot(LogNuArr, np.log10(Luminosity3(LogRArr, np.power(10, LogNuArr))))
plt.xlabel('$Log_{10}($\nu$)$ / $Hz$')
plt.ylabel('$Log_{10}(L)$ / $W$')
plt.show()