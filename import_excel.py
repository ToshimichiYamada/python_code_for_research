# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 20:00:07 2016

@author: Hiro
"""

import xlrd 
import pandas
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

# import data from excel 
if __name__ == '__main__' :
    book = xlrd.open_workbook ('C:/research/python/data/qPCR_decay.xlsx')
    sheet1 = book.sheet_by_name('qPCR')
    data1 = []
    data1 = [[sheet1.cell_value(r, col)
                for col in range(sheet1.ncols)]
                    for r in range(sheet1.nrows)]

    sheet2 = book.sheet_by_name('Bric')
    data2 = []
    data2 = [[sheet2.cell_value(r, col)
                for col in range(sheet2.ncols)]
                    for r in range(sheet2.nrows)]


# numbers are registered as numbers, while leaving the strings alone
for i in range (len (data1)):
    for j in range(len(data1[0])):
        try:
            data1[i][j] = float (data1[i][j])
        except:
            pass

for i in range (len (data2)):
    for j in range(len(data2[0])):
        try:
            data2[i][j] = float (data2[i][j])
        except:
            pass

# Wrap the data in a pandas DataFrame
df1 = DataFrame(data1[1:], columns = data1[0])
df2 = DataFrame(data2[1:], columns = data2[0])


# Expand to all data
x = range(7)
for i in x:

    # plot the mRNA decay
    plt.scatter(df1["time"], df1.ix[:,2 + 2*i], edgecolor = 'k', facecolor = 'gray', label = 'qPCR siCTRL', alpha = 0.5)
    plt.scatter(df1["time"], df1.ix[:,3 + 2*i], edgecolor = 'darkred', facecolor = 'r', label = 'qPCR siPUM1', alpha = 0.5)
    plt.scatter(df2["time"], df2.ix[:,2 + 2*i], marker = 'D', edgecolor = 'k', facecolor = 'gray', label = 'Bric siCTRL', alpha = 0.5)
    plt.scatter(df2["time"], df2.ix[:,3 + 2*i], marker = 'D', edgecolor = 'darkred', facecolor = 'r', label = 'Bric siPUM1', alpha = 0.5)
    plt.title(df1.ix[i,0] +' mRNA decay')
    plt.xlabel('Time')
    plt.ylabel('relative expression')
    plt.legend(loc = 3, fontsize = 8)
    plt.ylim(0.05,2.0)
    plt.xlim(-1,13)
    plt.yscale('log')
    plt.savefig(df1.ix[i,0] +' mRNA decay', dpi = 300)
    plt.close()