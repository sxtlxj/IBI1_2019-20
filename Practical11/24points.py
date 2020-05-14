# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 21:23:47 2020

@author: DM
"""

import itertools
import fractions
N = input("Please input numbers to compute24:(use ',' to divide them)\n")
M = N.split(",") 
for i in range(len(M)):                 
    M[i] = int(M[i]) #make input numbers as int saved in a list called M
    if M[i] >= 24:
        print("The input number must be integers from 1 to 23")
        exit()
L=len(M)

def compute(m,n): 
    '''
    operate +-*/ on m and n
    exclude the situation that devisor is 0
    '''
    if m!=0 and n!=0:
        z=[m+n,n-m,m-n,m*n,fractions.Fraction(m,n),fractions.Fraction(n,m)]         
    if m==0 and n!=0:
        z=[0,-n,n]
    if m!=0 and n==0:
        z=[0,-m,m]
    if m==0 and n==0:
        z=[0]
    return z

def enumeration(i):
    sequence=list(permutations[i]) #convert tuple into list
    y=compute(sequence[0],sequence[1])
    del sequence[0:2] 
    while sequence!=[]: #repeat until every number in 'sequence' is deleted ('computed')
        y_copy=y #make a copy of y because y is going to be changed        
        for j in y_copy:
            y+=compute(j,sequence[0]) #store newly obtained results in y
        del sequence[0] #delete the number in 'sequence' that just completes the 'compute' function
    
    return y

permutations=list(itertools.permutations(M)) #enumerate every permutation
permutations=list(set(permutations)) #delete the duplicates to diminish the computation
list1=[]
for i in range(len(permutations)): #repeat 'enumeration' for every possible order of inputted numbers
    list1+=enumeration(i) 
if 24 in list1:
    print('Yes')
else:
    print('No')    

recursion_time=(L-1)*len(list1) 
print('recursion times: '+ str(recursion_time))

    
    
