# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 14:26:13 2020

@author: DM
"""

#start with a number called x
x = input('give a number')
x = int(x)
#create the vairable ans to save the answer of the question
ans = "%d is " % x
#change x into binary form and save as a string called y
y = bin(x)

#list y so that can be shown separately in the final result
a = list(y)
#delete the first two useless element 
del a[0:2]

#ensure how long the bianry x is and save the result in z
z = len(a)
#write the binary compostition of x
for i in range(0,z):
    j = a[i]
    if j == "1":
            m=z-1-i
            ans = ans + "2**%d + "% m
            
#Delete the additional "+" at the end
space = ans.split()
print(space)
del space[-1]
ans = " ".join(space)          
#Finally print the result       
print(ans)