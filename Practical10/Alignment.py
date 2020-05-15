# -*- coding: utf-8 -*-
"""
Created on Thu May  7 21:44:04 2020

@author: DM
"""
import numpy as np
import pandas as pd
data = pd.read_excel("BLOSUM62.xlsx")
pd.set_option('display.width',None)

amino=""
for i in range(0,np.shape(data)[0]): # creat amino to save amino acid in data
    amino+=data.iloc[i,0]
    
#define a function called "readseq" to read given sequences
def readseq(filename):
    with open (filename,"r") as x:
        for line in x:
            if not line.startswith("<"):                
                seq = line.replace("\n","").strip()
        return(seq)
#use "readseq" to re input sequences
seq_human = readseq("SOD2_human.fa")
seq_mouse = readseq("SOD2_mouse.fa")
seq_random = readseq("RandomSeq.fa")


# define a function score to compare two sequences
def scores(a,b):
    distance=0
    identity=0
    score=0
    
    for i in range(len(a)): 
        row = amino.index(a[i])
        column=amino.index(b[i])+1    
        score+=data.iloc[row,column]  #select scores in BLOSUM62                                               
        if a[i] != b[i]: #count the hamming distance
            distance += 1
        else:
            identity+=1
                
    distance = distance 
    percent_a= identity/len(a)*100 # the similarity in percentage
    return( "distance: "+str(distance),          
           "identity: "+str(percent_a)+"%",
           "scores: "+str(score))
scores(seq_human,seq_mouse)
scores(seq_human,seq_random)
scores(seq_mouse,seq_random)
print(scores(seq_human,seq_mouse),scores(seq_human,seq_random),scores(seq_mouse,seq_random))

      



    

        