# -*- coding: utf-8 -*-
"""
Created on Thu Oct 08 14:27:04 2015

@author: Hiro
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(size = 2000)
y = np.random.normal(size = 2000)

plt.scatter(x, y, alpha = 0.3)

plt.title("scatterplot")
plt.xlabel("x")
plt.ylabel("y")

plt.show()