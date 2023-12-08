from cProfile import label
import numpy as np
import math

#region Constants
#####################################################################

# Constants    (FIND REFERENCES)
c = 299792458                               # metres per sec
G = 6.6743 * math.pow(10, -11) # 0.000000000066743                       # Neuton metres sqared per kg sqaured  
M_sol = 2 * math.pow(10, 30) # 2000000000000000000000000000000     # Kg
SB = 5.670374419 * math.pow(10, -8) # 0.0000005670374419                     # Stefan Boltzmann - Watt per square metre per Kelvin to forth
planck = 6.62607015 * math.pow(10,-34)           # Joules per Hertz
k_B = 1.380649 * math.pow(10,-23)           # Boltzmann - Joules per Kelvin
pi = 3.14159265358979323846264338327950288419716939
e = 2.7182818284590452353602874713527

# Galaxy Values
M = 10 * M_sol                              # Kg
Acc_rate = math.pow(10, 15)                 # Kg per sec

# R_g = (G * M) / (c**2) # ~14,852m               metres
R_g = 14852.32053823733
R_in = 6 * R_g                              # metres
R_out = 100000 * R_g                        # metres
r_in = 6
r_out = 100000

nu_st = math.pow(10, 14)
nu_end = math.pow(10, 19)
lognu_st = 14
lognu_end = 19

#endregion

#####################################################################

# region values
def MaxVal(y):
    i = np.argmax(y)
    return i+1

def unlog(x):
    return np.power(10, x)

def R_to_r (R):
    r = []
    for i in range(len(R)):
        r.append(R[i]/R_g)
    return r

def LogR_to_Logr (LogR):
    Logr = []
    for i in range(0,len(LogR)):
        Logr.append(LogR[i] - np.log10(R_g))
    return Logr
# endregion

#####################################################################

# region Radius and frequenecy arrays

Rsteps = 1001
LogRArr = np.linspace(np.log10(R_in),np.log10(R_out), Rsteps)
UnLogRArr = unlog(LogRArr)
UnLogRArr[0] = R_in + 1

nusteps = 1001
LogNuArr = np.linspace(lognu_st, lognu_end, nusteps)
UnLogNuArr = unlog(LogNuArr)

#endregion

#####################################################################

# region steps
# def LogRArrVar (steps):
#     return np.linspace(np.log10(R_in),np.log10(R_out), steps)
# def LogNuArrVar (steps):
#     return np.linspace(lognu_st, lognu_end, steps)
def UnLogRArrVar (steps):
    LogArr = np.linspace(np.log10(R_in), np.log10(R_out), steps)
    Arr = unlog(LogArr)
    Arr[0] = R_in + 1
    return Arr
def UnLogNuArrVar (steps):
    Arr = np.linspace(lognu_st, lognu_end, steps)
    return unlog(Arr)
# endregion

#####################################################################

# region Temperature functions
def Temp (R):
    constant = (G * M * Acc_rate) / (8 * pi * SB)
    T4 = constant * 1/(pow(R,3))
    return pow(T4, 0.25)

def TempViscR (R):
    constant = (3 * G * M * Acc_rate)/(8 * pi * SB)
    T4 = constant * (1/(pow(R, 3))) * (1 - math.pow((R_in/R), 0.5))
    return math.pow(T4, 0.25)
    
def TempArrFnc (fnc, R):
    arr = []
    for i in range(0,len(R)):
        arr.append(fnc(R[i]))
    return arr
# endregion

#####################################################################

# region Temperature variables

TempArr = TempArrFnc(Temp, UnLogRArr)
TempViscArr = TempArrFnc(TempViscR, UnLogRArr)
TempViscArr[0] = 0.0000000000000001

TMaxIndex = MaxVal(TempViscArr)

#endregion

#####################################################################

# region Flux functions
def Flux (Tfnc, nu, R):
    constant = (2 * pi * planck) / (c ** 2)
    exponent = (planck * nu) / (k_B * Tfnc(R))
    B_v = (constant * pow(nu, 3)) / (np.exp(exponent) - 1)
    return pi * B_v

def FluxVisc (R, nu):
    constant = (2 * pi * planck) / (math.pow(c, 2))
    exponent = (planck * nu) / (k_B * TempViscR(R))
    B_v = (constant * math.pow(nu, 3)) / (np.exp(exponent) - 1)
    return B_v

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
# endregion

#####################################################################

# region Integration functions
def integrate_xVar (x, y, var):
    total = 0
    for i in range(0, len(x)-1):
        h = abs(x[i+1] - x[i])
        total += h/6 * (y(x[i], var) + 4*y(x[i]+0.5*h, var) + y(x[i+1], var))
    return total

def integrate_xVar2 (x, y, var):
    total = 0
    for i in range(0, len(x)-1, 2):
        h = (x[i+2]-x[i]) / 6
        total += h * (y(x[i], var) + 4 * y(x[i+1], var) + y(x[i+2], var))
    return total

def integrate_Varx (x, y, var):
    total = 0
    for i in range(0, len(x)-1):
        h = abs(x[i+1] - x[i])
        total += h/6 * (y(var, x[i]) + 4*y(var, x[i]+0.5*h) + y(var, x[i+1]))
    return total

def integrate_Varx2 (x, y, var):
    total = 0
    for i in range(0, len(x)-1, 2):
        h = (x[i+2]-x[i]) / 6
        total += h * (y(var, x[i]) + 4 * y(var, x[i+1]) + y(var, x[i+2]))
    return total
# endregion

#####################################################################

# region Luminosity functions
def integrand (R, nu):
    return FluxVisc(R, nu) * 4 * pi * R

def Luminosity (R, nu):
    Lum = []
    for i in range(0, len(nu)):
        Lum.append(integrate_xVar2(R, integrand, nu[i]) * nu[i])
    return Lum

def LuminosityFnc (R, nu):
    return integrate_xVar(R, integrand, nu)

def LuminosityFnc2 (R, nu):
    return integrate_xVar2(R, integrand, nu)
# endregion

#####################################################################