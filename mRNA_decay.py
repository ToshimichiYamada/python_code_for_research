# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:09:23 2016

@author: Hiro
"""

import numpy as np
import matplotlib.pyplot as plt
import xlrd
from scipy.optimize import curve_fit

# import data from excel 
if __name__ == '__main__' :
    book = xlrd.open_workbook ('C:/research/python/data/qPCR_decay.xlsx')
    sheet = book.sheet_by_name('Sheet1')
    decay_con = []
    decay_si  = []    

    for row in range (1, sheet.nrows):
        value = sheet.cell(row, 3).value
        if value != '':
            decay_con.append(value)
    
    for row in range (1, sheet.nrows):
        value = sheet.cell(row, 4).value
        if value != '':
            decay_si.append(value)

Name_con = sheet.cell_value(0, 1)
Name_si = sheet.cell_value(0, 2)

print Name_si, decay_si

def fitFunc(t, tau):
    return np.exp(-1*t/tau)

#  Define Time
t_data = 0.0, 1.0, 2.0, 4.0, 8.0, 12.0

# Curve-fitting
fitParams_con, fitCovariances_con = curve_fit(fitFunc, t_data, decay_con)
fitParams_si, fitCovariances_si = curve_fit(fitFunc, t_data, decay_si)


# Results
print fitParams_con * np.log(2)
print fitParams_si * np.log(2)

# plot the data points and fit curve

plt.ylabel('relative expression', fontsize = 16)
plt.xlabel('Time(sec)', fontsize = 16)
plt.title('mRNA decay')

list_y_con = []
for num in t_data:
    list_y_con.append(np.exp(-1*num/fitParams_con))

list_y_si = []
for num in t_data:
    list_y_si.append(np.exp(-1*num/fitParams_si))
    
plt.yscale("log")
plt.xlim(-1,13)
plt.ylim(0.05, 1.5)
plt.scatter(t_data, decay_con, edgecolor = 'k', facecolor = 'gray', alpha = 0.8, s = 75)
plt.plot(t_data, np.array(list_y_con), 'k')
plt.scatter(t_data, decay_si, edgecolor = 'darkred', facecolor = 'red', alpha = 0.8, s = 75)
plt.plot(t_data, np.array(list_y_si), 'darkred')

plt.savefig('Decay_plot.tif', dpi = 300)

plt.show()
