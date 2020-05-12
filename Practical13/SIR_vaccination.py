# -*- coding: utf-8 -*-
"""
Created on Tue May 12 13:16:17 2020

@author: DM
"""

import matplotlib.pyplot as plt
import numpy as np


N=10000 #total number of people
β=0.3 # the infection rate upon contact
γ=0.005 #recovery probability
S=10000
I=0
R=0 # save the number of suspectible, infected and recovered people

SD=[10000]
ID=[0]
RD=[0]# make array for number after every taking
plt.figure(figsize=(6,4),dpi=150)




for x in range(0,11):
    S=9999
    I=1
    R=0 
    SD=[9999]
    ID=[1]
    RD=[0]#refresh the number at the start of every try
    V=int(10000*x/10)
    S=10000-V
    R=V
    for i in range(1000):
        proportion=I/N
        infection=np.random.choice(range(2),S,p=[1-β*proportion,β*proportion])#0 as not infected and 1 as infected
        recovery=np.random.choice(range(2),I,p=[1-γ,γ])#0 as not recovered and 1 as recovered
        S1=S
        I1=I
        for j in range(S1):
            if infection[j]==1:
                S=S-1
                I=I+1
        for k in range(I1):            
            if recovery[k]==1:
                R=R+1
                I=I-1
        ID.append(I)
            
    plt.plot(ID)
    
    


plt.title("SIR model with different vaccinated rate")
plt.xlabel("time")
plt.ylabel("number of people")
plt.legend(["0","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%"])
plt.savefig("SIR model with different vaccinated rate.png",bbox_inches="tight")
plt.show()
        
        
    
    
    