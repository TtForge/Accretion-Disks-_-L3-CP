from cProfile import label
import matplotlib.pyplot as plt
# from __FunctionBase import *
from Testing.__FunctionBase import *

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

colours = ['#FFF9DD', '#FEE28B', '#FFCB58', '#FFAC2B', '#F98811', '#E16904', '#CE4F01', '#A02A00', '#641400']

# FreqLabels = [$\\nu = 10^{0}$', '$\\nu = 10^{1}$', '$\\nu = 10^{2}$', '$\\nu = 10^{3}$', '$\\nu = 10^{4}$', '$\\nu = 10^{5}$', '$\\nu = 10^{6}$', '$\\nu = 10^{7}$', '$\\nu = 10^{8}$', '$\\nu = 10^{9}$', '$\\nu = 10^{10}$', '$\\nu = 10^{11}$', '$\\nu = 10^{12}$', '$\\nu = 10^{13}$', '$\\nu = 10^{14}$', '$\\nu = 10^{15}$', '$\\nu = 10^{16}$', '$\\nu = 10^{17}$', '$\\nu = 10^{18}$', '$\\nu = 10^{19}$', '$\\nu = 10^{20}$', '$\\nu = 10^{21}$', '$\\nu = 10^{22}$']
FreqLabels = []
for i in range(0,23):
    FreqLabels.append('$\\nu = 10^{' + str(i) + '}$')



