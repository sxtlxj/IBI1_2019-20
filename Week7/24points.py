# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 21:23:47 2020

@author: DM
"""

import random
N = input("Please input numbers to compute24:(use ',' to divide them)\n")

print(N)
M = N.split(",") 
for i in range(len(M)):
                 
    M[i] = int(M[i])
    if M[i] >= 24:
        print("The input number must be integers from 1 to 23")
        break



    
    
