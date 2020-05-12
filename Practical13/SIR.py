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
S=9999
I=1
R=0 # save the number of suspectible, infected and recovered people
SD=[10000]
ID=[0]
RD=[0]# make array for number after every taking

for i in range(1000):
    proportion=I/N    
    infection=np.random.choice(range(2),S,p=[1-β*proportion,β*proportion])#0 as not infected and 1 as infected
    recovery=np.random.choice(range(2),I,p=[1-γ,γ])#0 as not recovered and 1 as recovered
    S1=S
    I1=I #save for the reason that S and I will change in the next step
    for j in range(S1):
        if infection[j]==1:
            S=S-1
            I=I+1
    for k in range(I1):
        if recovery[k]==1:
            R=R+1
            I=I-1
    SD.append(S)
    ID.append(I)
    RD.append(R)

plt.figure(figsize=(6,4),dpi=150)
plt.plot(SD)
plt.plot(ID)
plt.plot(RD)
plt.title("SIR model")
plt.xlabel("time")
plt.ylabel("number of people")
plt.legend(["susceptible","infected","recovered"])

plt.savefig("SIRmodeloutcome.png",bbox_inches="tight")
plt.show()
        
        
    
    
    