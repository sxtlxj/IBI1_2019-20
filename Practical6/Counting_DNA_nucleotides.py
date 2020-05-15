# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:09:33 2020

@author: DM
"""

import matplotlib.pyplot as plt

DNA = input('give me a sequence of DNA: ')  #ask to input DNA
counterA = 0 #set the initial counter as 0
counterT = 0
counterC = 0
counterG = 0
for i in range(len(DNA)): #count all nucleotides
    if DNA[i] == 'A':
        counterA = counterA + 1
    elif DNA[i] == 'T':
        counterT = counterT + 1
    elif DNA[i] == "C":
        counterC = counterC + 1
    else:
        counterG = counterG + 1

frequency = {'A': counterA, 'C': counterC, 'T': counterT, 'G': counterG} #create a dictionart to save counters
print(frequency)        
        
            
# define the elements of the pie chart
labels = 'A', 'T', 'C', 'G'
sizes = [counterA, counterT, counterC, counterG]


fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', #show result in one decimal
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('pie of the four DNA nucleotides')
plt.show()