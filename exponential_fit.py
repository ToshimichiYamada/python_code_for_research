# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:24:21 2016

This is a template for
curve-fitting the data of mRNA decay measured by qPCR

"""

# define a fitting function
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fitFunc(t, tau):
    return np.exp(-1*t/tau)

# ｄａｔａ　ｓｅt
t_data = 0.0, 1.0, 2.0, 4.0, 8.0, 12.0
rel_amount = 1.0, 0.8, 0.4, 0.2, 0.1, 0.4

# Curve-fitting
fitParams, fitCovariances = curve_fit(fitFunc, t_data, rel_amount)

# Results
print fitParams
print fitCovariances
print fitParams * np.log(2)

# plot the data points and fit curve

plt.ylabel('relative expression', fontsize = 16)
plt.xlabel('Time(sec)', fontsize = 16)
plt.title('mRNA decay')

list_y = []
for num in t_data:
    list_y.append(np.exp(-1*num/fitParams))
    
plt.yscale("log")
plt.xlim(-1,13)
plt.ylim(0.01, 1.5)
plt.scatter(t_data, rel_amount)
plt.plot(t_data, np.array(list_y))

plt.savefig('Decay_plot.tif', dpi = 300)

plt.show()