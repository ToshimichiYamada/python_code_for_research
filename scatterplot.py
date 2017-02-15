# -*- coding: utf-8 -*-
"""
Created on Thu Oct 08 10:58:42 2015

@author: Hiro
"""

import numpy as np
import xlrd
import matplotlib.pyplot as plt

def get_data(sheet, rowx, colx):
    data = []
    for row in range (rowx. sheet.nrows):
        value = sheet. cell(row, colx).value
        if value != '':
            data.append(value)
            
        data = np.array(data)
    return data

if __name__ == '_main__':
    book = xlrd.open_workbook ('C:/research/python/data/Briq_seq_151006.xlsx')
    sheet = book.sheet_by_name('sheet3')
    data1 = get_data(sheet, 1, 8) 
    data2 = get_data(sheet, 1, 7)
    
    plt.scatter(data1, data2, s = 25, alpha = 0.4, marker = 'o', color = 'b')
    
    plt.xlim(-2, 5)
    plt.ylim(-2, 5)
        
    plt.xlabel('halftime siSte (rpkm)', size = 14)    
    plt.ylabel('halftime siCTRL (rpkm)', size = 14)
    
    plt.show()
