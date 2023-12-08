from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import integrate as integ

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

def MaxVal(y):
    i = np.argmax(y)
    return i+1

def unlog(x):
    return np.power(10, x)

#####################################################################

Rsteps = 1001
LogRArr = np.linspace(np.log10(R_in),np.log10(R_out), Rsteps)
UnLogRArr = unlog(LogRArr)
UnLogRArr[0] = R_in + 1
def LogRArrVar (steps):
    return np.linspace(np.log10(R_in),np.log10(R_out), steps)

nusteps = 1001
LogNuArr = np.linspace(lognu_st, lognu_end, nusteps)
UnLogNuArr = unlog(LogNuArr)
def LogNuArrVar (steps):
    return np.linspace(lognu_st, lognu_end, steps)

#region Temp fncs
#####################################################################
### Temperature Functions ###########################################

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

TempArr = TempArrFnc(Temp, UnLogRArr)
TempViscArr = TempArrFnc(TempViscR, UnLogRArr)
TempViscArr[0] = 0.0000000000000001

TMaxIndex = MaxVal(TempViscArr)

# print(UnLogRArr[MaxVal(TempViscArr)]/R_g)
# print(TempViscArr[MaxVal(TempViscArr)])


#endregion
'''
#region Temp plotting
#####################################################################
### Temperature Plotting ############################################

# plt.style.use('dark_background')
plt.rcParams.update({
    "figure.facecolor":  (1.0, 1.0, 1.0, 0.0),  # red   with alpha = 30%
    "axes.facecolor":    (1.0, 1.0, 1.0, 0.0),  # green with alpha = 50%
    "savefig.facecolor": (1.0, 1.0, 1.0, 0.0),  # blue  with alpha = 20%
    "legend.framealpha": 0.2,
    "lines.linewidth":   3,
    "axes.linewidth":    3,
    "axes.labelsize":    20,
    "lines.markersize": 10,
    "xtick.labelsize": 16,
    "ytick.labelsize": 16,
    "legend.fontsize": 15,
    "axes.edgecolor": 'white',
    "xtick.labelcolor": 'white',
    "ytick.labelcolor": 'white',
    "axes.labelcolor": 'white',
    "legend.labelcolor": 'white',
    "text.color": 'white',
    "axes.spines.top":    False,
    "axes.spines.right":  False,
    "ytick.color": 'white',
    "legend.markerscale": 2,
    "font.family": 'serif',
    "mathtext.fontset": 'dejavuserif',
    "savefig.format": 'svg',
})

plt.plot(LogR_to_Logr(LogRArr), TempArr, label = "Temp")
plt.plot(LogR_to_Logr(LogRArr), TempViscArr, label = "Temp + Visc")
plt.xlabel('Log(Radius / $R_g$)')
plt.ylabel('Temperature / $K$')
plt.legend()
plt.savefig('Graphs\Temp vs logr.svg', format='svg')
plt.show()

'''
'''plt.plot(LogR_to_Logr(LogRArr), TempViscArr_r, label = "Temp + Visc")
plt.xlabel('Log(Radius / $R_g$)') 
plt.ylabel('Temperature / $K$')
plt.legend()
plt.show()'''
'''

#endregion
'''
#region Flux fncs + plotting 
#####################################################################
### Flux Functions + Plotting #######################################

'''
def Flux(T, nu):
    constant = (2 * pi * planck) / (c ** 2)
    exponent = (planck * nu) / (k_B * T)
    B_v = (constant * pow(nu, 3)) / (np.exp(exponent) - 1)
    return pi * B_v
    
def FluxArray (T, nu):
    FluxArr = []
    for i in range(0, len(T)):
        FluxArr.append(Flux(T[i], nu))
    return FluxArr
'''

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
'''
for i in range(14, 20):
    plt.plot(LogR_to_Logr(LogRArr), np.log10(FluxArrViscFnc(UnLogRArr, math.pow(10,i))), label = "v = 10^" + str(i) + ' Hz')
plt.xlabel('Log(Radius / $R_g$)')
plt.ylabel('Log(Flux / $W m^{-2}$)')
plt.legend()
plt.savefig('Graphs\LogLog Flux vs r.svg', format='svg')
plt.show()
'''
#endregion

#region Flux vs Temp Plotting
#####################################################################
### Flux vs Temp Plotting ###########################################
'''
for i in range (14, 20):
    plt.scatter(np.log10(TempViscArr[TMaxIndex:]), np.log10(FluxArrViscFnc(UnLogRArr, math.pow(10,i))[TMaxIndex:]), label = ("v = 10^" + str(i) + ' Hz'), marker = 'x', s=10,  linewidth=0.5)
    # plt.plot(TempViscArr, np.log10(FluxArray(TempViscArr, pow(10, i))), label = ("v = 10^" + str(i)))
plt.xlabel('Temperature / $K$')
plt.ylabel('Log(Flux / $W m^{-2}$)')
plt.legend()
plt.show()

for i in range (14, 20):
    plt.scatter(TempViscArr, FluxArrViscFnc(UnLogRArr, math.pow(10,i)), label = "v = 10^" + str(i) + ' Hz', marker = 'x', s=10, linewidth=0.5)
    # plt.plot(TempViscArr, FluxArray(TempViscArr, pow(10, i)), label = "v = 10^" + str(i))
plt.xlabel('Temperature / $K$')
plt.ylabel('Flux / $W m^{-2}$')
plt.legend()
plt.show()
'''
#endregion

#region Integration and Luminosity Functions
#####################################################################
### Integration and Luminosity Functions ############################

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

def integrand (R, nu):
    return FluxVisc(R, nu) * 4 * pi * R

def Luminosity (R, nu):
    Lum = []
    for i in range(0, len(nu)):
        Lum.append(integrate_xVar(R, integrand, nu[i]) * nu[i])
    return Lum

def LuminosityFnc (R, nu):
    return integrate_xVar(R, integrand, nu)

def LuminosityFnc2 (R, nu):
    return integrate_xVar2(R, integrand, nu)


def SciIntegrate (fnc, a_low, a_high, b):
    temporary = integ.quad(fnc, a_low, a_high, args=(b,))
    return temporary[0]

def SciIntegrate2 (fnc, a_low, a_high):
    temporary = integ.quad(fnc, a_low, a_high)
    return temporary[0]

def Luminosity_Sci (nu):
    Lum = []
    for i in range(0, len(nu)):
        Lum.append(SciIntegrate(integrand, R_in, R_out, nu[i]) * nu[i])
    return Lum

def Luminosity_Sci_Fnc (nu):
    return SciIntegrate(integrand, R_in, R_out, nu)

#endregion

#region Unused Function
#####################################################################
### Unused Functions ################################################
'''
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
        h = abs(nu[i+1] - nu[i])
        total += h/3 * (Lum(LogR, nu[i]) + 4* Lum(LogR, nu[i]+0.5*h) + Lum(LogR, nu[i] + h))
    return total

def integrate_Lum2 (nu, Lum, LogR):
    total = 0
    steps = int(len(nu) / 2)
    for i in range(0, steps-1):
        h = nu[i+1] - nu[i]
        total += h/3 * (Lum(LogR, nu[2*i]) + 4 * Lum(LogR, nu[2*i+1]) + Lum(LogR, nu[2*i+2]))
    return total

############################# small r fncs

def TempViscr (r):
    constant = (3 * G * M * Acc_rate)/(8 * pi * SB * (R_g **3))
    T4 = constant * (1 / (math.pow(r,3))) * (1 - math.pow((r_in/r), 0.5))
    return math.pow(T4, 0.25)

TempViscArr_r = TempArrFnc(TempViscr, R_to_r(UnLogRArr))
TempViscArr_r[0] = 0.0000000000000001

def FluxViscr (r, nu):
    constant = (2 * pi * planck) / (math.pow(c, 2))
    exponent = (planck * nu) / (k_B * TempViscr(r))
    B_v = (constant * pow(nu, 3)) / (np.exp(exponent) - 1)
    return pi * B_v

def integrandr (r, nu):
    return FluxViscr(r, nu) * 4 * pi * math.pow(R_g,2) * r

def Luminosity_Sci_Fncr (nu):
    return SciIntegrate(integrandr, r_in, r_out, nu)

Lum_Tot_Scir = SciIntegrate2(Luminosity_Sci_Fncr, nu_st, nu_end)
print('Total Luminosity w/ 1000 $\\nu$ steps using Sci = ' + str(Lum_Tot_Scir))
'''
#endregion
'''
#region Integrand Plotting
#####################################################################
### Integrand Plotting ##############################################

plt.figure(figsize= (6.4,2.5))
for z in range(14,20):
    IntegrandArr = []
    for i in range(len(UnLogRArr)):
        IntegrandArr.append(integrand(UnLogRArr[i], math.pow(10,z)))
    plt.scatter(LogR_to_Logr(LogRArr), np.log10(IntegrandArr), label = 'v = 10^' + str(z) + ' Hz', marker = 'x', s=10, linewidth=0.5)
# plt.xlabel('Log($Radius$ / $R_g$)')
# plt.ylabel('Log($d(L_{\\nu})/dR$ / $Wm$)')
# plt.legend(bbox_to_anchor=(1,0.7))
plt.ylim(-3, 10)
plt.savefig('Graphs\LogLog cropped Integrand vs r.svg', format='svg')
plt.show()

for z in range(14,20):
    IntegrandArr = []
    for i in range(len(UnLogRArr)):
        IntegrandArr.append(integrand(UnLogRArr[i], math.pow(10,z)))
    plt.scatter(LogR_to_Logr(LogRArr), np.log10(IntegrandArr), label = 'v = 10^' + str(z) + ' Hz', marker = 'x', s=10, linewidth=0.5)
plt.xlabel('Log($Radius$ / $R_g$)')
plt.ylabel('Log($d(L_{\\nu})/dR$ / $Wm$)')
plt.legend(loc = 'lower left', prop={'size': 10}) # bbox_to_anchor=(1,0.7))
plt.savefig('Graphs\LogLog Integrand vs r.svg', format='svg')
plt.show()

#endregion
'''
#region Luminosity Total and plotting
#####################################################################
### Luminosity Total and Plotting ###################################

# vLum_vals1 = Luminosity(LogRArr[:TMaxIndex], np.power(10, LogNuArr[:TMaxIndex]))
# plt.plot(LogNuArr[:TMaxIndex], np.log10(vLum_vals1))
'''
############### Manual Integral
vLum_vals2 = Luminosity(UnLogRArr[TMaxIndex:], UnLogNuArr[TMaxIndex:])
plt.plot(LogNuArr[TMaxIndex:], np.log10(vLum_vals2))
plt.xlabel('Log($\\nu$ / $Hz$)')
plt.ylabel('Log($\\nu L_{\\nu}$ / $W Hz$)')
plt.savefig('Graphs\LogLog nuL vs nu.svg', format='svg')
plt.show()
'''
############### Total luminosity manual
# Lum_Tot = integrate_Varx(UnLogNuArr[TMaxIndex:], LuminosityFnc, UnLogRArr[TMaxIndex:]) # integrate_Lum(np.power(10, LogNuArr[:TMaxIndex]), LuminosityFnc, LogRArr[:TMaxIndex]) +
# print('Total Luminosity w/ 1000 $\\nu$ & R steps = ' + str(Lum_Tot)) 

Lum_Tot = integrate_Varx2(UnLogNuArr, LuminosityFnc2, UnLogRArr) # integrate_Lum(np.power(10, LogNuArr[:TMaxIndex]), LuminosityFnc, LogRArr[:TMaxIndex]) +
print('Total Luminosity w/ 1000 $\\nu$ & R steps = ' + str(Lum_Tot)) 


'''############### Scipy Integral
vLum_vals_sci = Luminosity_Sci(UnLogNuArr)
plt.plot(LogNuArr, np.log10(vLum_vals_sci)) # [TMaxIndex:]
plt.xlabel('Log($\\nu$ / $Hz$)')
plt.ylabel('Log($\\nu L_{\\nu}$ / $W Hz$)')
plt.show()

# print(np.log10(vLum_vals_sci))
# print(LogNuArr)
print(vLum_vals_sci[804:807])
print(LogNuArr[804:807])'''

############## Total luminosity Scipy
# Lum_Tot_Sci = SciIntegrate2(Luminosity_Sci_Fnc, nu_st, nu_end)
# print('Total Luminosity w/ 1000 $\\nu$ steps using Sci = ' + str(Lum_Tot_Sci))


# Lum_Tot2 = integrate_Lum2(np.power(10, LogNuArr[:TMaxIndex]), LuminosityFnc, LogRArr[:TMaxIndex]) + integrate_Lum2(np.power(10, LogNuArr[TMaxIndex:]), LuminosityFnc, LogRArr[TMaxIndex:])
# print('Integrate 2 = ' + str(Lum_Tot2))

"""
Lum_Log_Totals = []
Lum_Totals = []
steps = [100, 150, 200, 250, 300, 350, 400, 500, 600, 800, 1000, 1200, 1500, 2000]
for i in steps:
    LumTotal = integrate_Varx(unlog(LogNuArrVar(i)[TMaxIndex:]), LuminosityFnc, LogRArrVar(i)[TMaxIndex:])
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