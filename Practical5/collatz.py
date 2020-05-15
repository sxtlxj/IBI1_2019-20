# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:51:46 2020

@author: DM
"""

n = 25 #input n This time I used example 25
print(n)
while n != 1: #start while loop and exit when the output is 1
    if n%2==0: #check whether n is a even or odd
        n=n/2 #n is even and then it is devided by 2
        print(n)
    else:
        n=n*3+1 # n is odd and then it is multiplied by 3 and added by 1
        print(n)
        