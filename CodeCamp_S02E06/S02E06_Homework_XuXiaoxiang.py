# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 08:20:56 2021

@author: XXU5SZH
"""

import os
import numpy as np
import pandas as pd

try:
    """Get folder address the py file located"""
    adrFolder = os.getcwd()
    
    """Open 4_0.txt and read into a list"""
    with open(adrFolder + "\\4_0.txt", 'r', encoding = 'utf-8-sig') as f:
        listWarpage = f.readlines()

    """Translate str to float(None if null)"""
    listResult = []
    for i in range(2, len(listWarpage)):
        s = listWarpage[i].split('\t')
        for j in range(0,len(s)):
            s[j] = s[j].strip()
            if s[j] == '':
                s[j] = None
            else:
                s[j] = float(s[j].replace(',', '.'))
        print(s)
        listResult.append(s)
    
    """Find the max and average value in column z: Option 1"""
    # listZvalue = []
    # for x in listResult:
    #     zValue = x[1] if x[1] else 0
    #     listZvalue.append(zValue)
    #     zValue = x[3] if x[3] else 0
    #     listZvalue.append(zValue)
    # maxZvalue, avgZvalue = max(listZvalue), sum(listZvalue)/len(listZvalue)
    
    """Option 2 with array and dataframe"""
    # pd.set_option('precision', 12)
    frame = pd.DataFrame(np.append(np.array(listResult)[:,1],np.array(listResult)[:,3]))
    frame.fillna(value={0:0}, inplace = True)
    maxZvalue, avgZvalue = frame[0].max(), frame[0].mean()
    
    """write the result to result.txt in the same folder as .py, generate if not exist"""
    result = 'max value in column z: {:,.12f}\naverage value in column z: {:,.12f}'\
        .format(maxZvalue, avgZvalue)   
    # print(result)
    with open(adrFolder + "\\result.txt", 'w', encoding = 'utf-8') as f:
        f.write(result)
    
except FileNotFoundError:
    print("'4_0.txt' can not be found in the folder: {}".format(adrFolder))


