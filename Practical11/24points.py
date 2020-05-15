# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 21:23:47 2020

@author: DM
"""

import fractions #import fractions to avoid floats

def calculate(numbers): #recursive function
    global found
    global times
    if numbers[len(numbers)-1]==24:#first check the number newly generated         
        found=True
        return
    if len(numbers)==1:
        return
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):            
            numbers_except=[]
            for k in range(0,len(numbers)):
                if k!=i and k!=j:
                    numbers_except.append(numbers[k])   #create a list without number[i] and number[j]        

            #operate "+-*/" on number[i] and number[j]
            
            #+
            numbers_next=numbers_except+[numbers[i]+numbers[j]]
            calculate(numbers_next) #use recursion until there is only one element remaining
            times+=1
                    
            #-
            if found==False:
                numbers[i]>numbers[j]
                numbers_next=numbers_except+[abs(numbers[i]-numbers[j])] #only generate positive numbers
                calculate(numbers_next)
                times+=1
                
                    
            #*
            if found==False:
                numbers_next=numbers_except+[numbers[i]*numbers[j]]
                calculate(numbers_next)
                times+=1
                
            #/
            if found==False:
                if numbers[j]!=0: #devisor cannot be 0
                    numbers_next=numbers_except+[fractions.Fraction(numbers[i]/numbers[j])]
                    calculate(numbers_next)
                    times+=1
                if numbers[i]!=0:
                    numbers_next=numbers_except+[fractions.Fraction(numbers[j]/numbers[i])]
                    calculate(numbers_next)
                    times+=1
    return

#with calculate() function, we can start to calculate 24 points
N = input("Please input numbers to compute24:(use ',' to divide them)\n")
M = N.split(",") 
for i in range(len(M)):                 
    M[i] = int(M[i]) #make input numbers as int saved in a list called M
    if M[i] >= 24 or M[i]<1:
        print("The input number must be integers from 1 to 23")
        break

found=False
times=0
calculate(M)
if found:
    print('Yes')
else:
    print('No')
print('recursion times: '+str(times))


    
    
