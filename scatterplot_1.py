# -*- coding: utf-8 -*-
"""
Created on Thu Oct 08 14:29:22 2015

@author: Hiro
"""

import numpy as np
import matplotlib.pyplot as plt
import xlrd

if __name__ == '__main__' :
    book = xlrd.open_workbook ('C:/research/python/data/Briq_151006.xlsx')
    sheet = book.sheet_by_name('Sheet1')
    x = []
    
    for row in range (1, sheet.nrows):
        value = sheet.cell(row, 2).value
        if value != '':
            x.append(value)

if __name__ == '__main__' :
    book = xlrd.open_workbook ('C:/research/python/data/Briq_151006.xlsx')
    sheet = book.sheet_by_name('Sheet1')
    y = []
    
    for row in range (1, sheet.nrows):
        value = sheet.cell(row, 1).value
        if value != '':
            y.append(value)

if __name__ == '__main__' :
    book = xlrd.open_workbook ('C:/research/python/data/Briq_151006.xlsx')
    sheet = book.sheet_by_name('Sheet1')
    r2 = []
    
    for row in range (1, sheet.nrows):
        value = sheet.cell(row, 3).value
        if value != '':
            r2.append(value)


plt.scatter(x, y, s = 25, c = r2, alpha = 0.1, marker = 'o', )
    

plt.xlabel('halftime siCTRL (rpkm)', size = 14)    
plt.ylabel('halftime siSte (rpkm)', size = 14)
    
plt.show()