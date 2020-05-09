# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 21:23:47 2020

@author: DM
"""

import random
N = input("Please input numbers to compute24:(use ',' to divide them)\n")
N = N.split(",")
print(N)
for i in range(len(N)):                  
    N[i] = int(N[i])
    if N[i] >= 24:
        print("The input number must be integers from 1 to 23")
        break

    
    
