# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:22:46 2020

@author: DM
"""
import re
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as xfile:
    
   
    for line in xfile:
        if line.startswith('>'):
            line = line.rstrip()
           
            
            name = re.findall(r'gene:(.*)gene_biotype',line)
            print(name,length)
        
        
            
            
            
                
                 
                
            