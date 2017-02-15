# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 19:17:08 2016

Robust nonlinear regression in scipy
"""

import numpy as np
import matplotlib.pyplot as plt


# Define data generator:

def generate_data(t, A, sigma, omega, noise=0, n_outliers=0, random_state=0):
    y = A * np.exp(-sigma * t) * np.sin(omega * t)
    rnd = np.random.RandomState(random_state)
    error = noise * rnd.randn(t.size)
    outliers = rnd.randint(0, t.size, n_outliers)
    error[outliers] *= 35
    return y + error

# Define model parameters:

A = 2
sigma = 0.1
omega = 0.1 * 2 * np.pi
x_true = np.array([A, sigma, omega])

noise = 0.1

t_min = 0
t_max = 30

# Data for fitting the parameters will contain 3 outliers:

t_train = np.linspace(t_min, t_max, 30)
y_train = generate_data(t_train, A, sigma, omega, noise=noise, n_outliers=4)

# Define the function computing residuals for least-squares minimization:

def fun(x, t, y):
    return x[0] * np.exp(-x[1] * t) * np.sin(x[2] * t) - y

# Use all ones as the initial estimate.

x0 = np.ones(3)

from scipy.optimize import least_squares
# Run standard least squares:

res_lsq = leastsq(fun, x0, args=(t_train, y_train))

# Run robust least squares with loss='soft_l1', set loss_scale to 0.1 which means that inlier residuals are approximately lower than 0.1.

res_robust = leastsq(fun, x0, loss='soft_l1', loss_scale=0.1, args=(t_train, y_train))

# Define data to plot full curves.

t_test = np.linspace(t_min, t_max, 300)
y_test = generate_data(t_test, A, sigma, omega)

# Compute predictions with found parameters:

y_lsq = generate_data(t_test, *res_lsq.x)
y_robust = generate_data(t_test, *res_robust.x)

# plot

plt.plot(t_train, y_train, 'o', label='data')
plt.plot(t_test, y_test, label='true')
plt.plot(t_test, y_lsq, label='lsq')
plt.plot(t_test, y_robust, label='robust lsq')
plt.xlabel('$t$')
plt.ylabel('$y$')
plt.legend()

plt.show()
