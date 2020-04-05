# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:22:46 2020

@author: DM
"""
import re
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as xfile:
     
    seq = {}
    for line in xfile:
        if line.startswith('>'):
            line = line.rstrip()
           
            
            name = str(re.findall(r'gene:(.*)gene_biotype',line))
            count = ''
            length = 0
            ls = []
        else:
            
            count += line.replace('\n','').strip()
            
            length += len(count)
            ls = [count, length]
            seq[name] = ls
    print(seq)
        
        
            
            
            
                
                 
                
            