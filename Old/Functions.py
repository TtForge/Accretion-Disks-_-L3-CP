from cProfile import label
from distutils.log import Log
from random import lognormvariate
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math
import scipy as sci

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



def Temp (R):
    constant = (G * M * Acc_rate) / (8 * np.pi * SB)
    T4 = constant * 1/(pow(R,3))
    return pow(T4, 0.25)

def TempViscR (R):
    constant = (3 * G * M * Acc_rate)/(8 * np.pi * SB)
    T4 = constant * 1/(pow(R,3)) * (1 - pow((R_in/R), 0.5))
    return pow(T4, 0.25)



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



def integrate (x, y, nu):
    total = 0
    for i in range(0, len(x)-1):
        h = x[i+1] - x[i]
        total += h * (y(x[i], nu) + 4*y(x[i]+0.5*h, nu)+y(x[i]+h, nu))
    return 1/6 * total

def integrate_Lum (nu, Lum, LogR):
    total = 0
    for i in range(0, len(nu)-1):
        h = nu[i+1] - nu[i]
        total += h * (Lum(LogR, nu[i]) + 4* Lum(LogR, nu[i]+0.5*h) + Lum(LogR, nu[i] + h))
    return 1/6 * total

def integrand(R, nu):
    return Flux(Temp(R), nu) * 4 * np.pi * R

def Luminosity (R, nu):
    Lum = []
    for i in range(0, len(nu)):
        Lum.append(integrate(np.power(10, R), integrand, nu[i]) * nu[i])
    return Lum

def LuminosityFnc(R, nu):
    return integrate(np.power(10, R), integrand, nu)