# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 16:56:53 2016

Liner-Regression
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas 
from pandas import DataFrame, Series
import statsmodels.formula.api as sm
from sklearn.linear_model import LinearRegression
import scipy, scipy.stats



data_str = '''0.0 1.0 2.0 4.0 8.0 12.0
1.0 0.8 0.4 0.2 0.1 0.4'''

# Split the string over the newlines, and then split each datum with space
d = data_str.split('\n')
d = [i.split(' ') for i in d]

# numbers are registered as numbers, while leaving the strings alone
for i in range (len (d)):
    for j in range(len(d[0])):
        try:
            d[i][j] = float (d[i][j])
        except:
            pass

#wrap the data in a Pandas Series
s = Series(data = d, index = ['t_data', 'rel_exp'])

print s

plt.scatter(s[0], s[1])

plt.show()

# Ordinary Least Squares Regression using Pandas and Statsmodels
Y = s[1]
X = s[0]
result = sm.OLS(Y, X).fit()
result.summary()
