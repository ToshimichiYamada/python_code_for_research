# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 17:42:34 2016

@author: Hiro
"""

import xlrd 
import pandas
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

# import data from excel 
if __name__ == '__main__' :
    book = xlrd.open_workbook ('C:/research/python/data/Bric_seq_160119.xlsx')
    sheet1 = book.sheet_by_name('PUM1')
    data1 = []
    data1 = [[sheet1.cell_value(r, col)
                for col in range(sheet1.ncols)]
                    for r in range(sheet1.nrows)]


# numbers are registered as numbers, while leaving the strings alone
for i in range (len (data1)):
    for j in range(len(data1[0])):
        try:
            data1[i][j] = float (data1[i][j])
        except:
            pass

# Wrap the data in a pandas DataFrame
df1 = DataFrame(data1[1:], columns = data1[0])

# extracting the mRNAs of which RPKM significantly increase 
df1.insert(3, 'RPKM_siSte_up', int)
df1['RPKM_siSte_up'] = df1['RPKM_siSte']
num = len(df1.index)
for i in range(num):
    if df1.ix[i,'log2(fold_change)'] < 0 or df1.ix[i,'q_value'] > 0.1:
        df1.ix[i,'RPKM_siSte_up'] = float('nan')

df1.insert(5, 'RPKM_siPUM1_up', int)
df1['RPKM_siPUM1_up'] = df1['RPKM_siPUM1']
num = len(df1.index)
for i in range(num):
    if df1.ix[i,'log2(fold_change)'] < 0 or df1.ix[i,'q_value'] > 0.1:
        df1.ix[i,'RPKM_siPUM1_up'] = float('nan')

# extracting the mRNAs of which RPKM significantly decrease 
df1.insert(4, 'RPKM_siSte_down', int)
df1.insert(7, 'RPKM_siPUM1_down', int)

df1['RPKM_siSte_down'] = df1['RPKM_siSte']
num = len(df1.index)
for i in range(num):
    if df1.ix[i,'log2(fold_change)'] > 0 or df1.ix[i,'q_value'] > 0.1:
        df1.ix[i,'RPKM_siSte_down'] = float('nan')

df1['RPKM_siPUM1_down'] = df1['RPKM_siPUM1']
num = len(df1.index)
for i in range(num):
    if df1.ix[i,'log2(fold_change)'] > 0 or df1.ix[i,'q_value'] > 0.1:
        df1.ix[i,'RPKM_siPUM1_down'] = float('nan')

# plot the result
plt.scatter(df1['RPKM_siSte'], df1['RPKM_siPUM1'], color = 'k',alpha = 0.2)
plt.scatter(df1['RPKM_siSte_up'], df1['RPKM_siPUM1_up'], color = 'red', alpha = 0.2)
plt.scatter(df1['RPKM_siSte_down'], df1['RPKM_siPUM1_down'], color = 'blue', alpha = 0.2)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('RPKM_siSte (log)')
plt.ylabel('RPKM_siPUM1 (log)')
plt.show()
