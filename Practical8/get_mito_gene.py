# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:22:46 2020

@author: DM
"""
import re
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as xfile: #open the given file
     
    seq = {}
    length1={} #create lists to save the sequences and lengths of sequences
    for line in xfile:
        if line.startswith('>'): 
            line = line.rstrip()  #delete spaces                   
            name = str(re.findall(r'gene:(.*)gene_biotype',line)) #target the gene name
            count = ''
            length = 0
            
        else:
            
            count += line.replace('\n','').strip() #make sequences in one line
            
            length += len(count)
            
            seq[name] = count
            length1[name]=length
#output the result as a new file 
with open('mito_gene.fa','w') as l:
    _str=""
    for key in seq.keys():    
        
        _str+=">"+ "%s %d"%(key,length1[key])+ "\n" + "%s"%(seq[key]) + "\n"

    l.writelines(_str)
    
    
            

        
        
            
            
            
                
                 
                
            