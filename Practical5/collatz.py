# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:51:46 2020

@author: DM
"""

j = 25
print(j)
while j != 1:
    if j%2==0:
        j=j/2
        print(j)
    else:
        j=j*3+1
        print(j)
        