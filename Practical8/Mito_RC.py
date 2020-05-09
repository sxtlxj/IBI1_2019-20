# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:48:39 2020

@author: DM
"""
# combine the task1 and 2 together
import re
filename = input(('Enter the file name: '))
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as xfile:
     
    seq = {}
    length1={}
    rc={}
    for line in xfile:
        if line.startswith('>'):
            line = line.rstrip()                     
            name = str(re.findall(r'gene:(.*)gene_biotype',line))
            count = ''
            length = 0
            
        else:
            
            count += line.replace('\n','').strip()
            
            length += len(count)
            
            seq[name] = count
            length1[name]=length
    for key in seq.keys():
        re = seq[key][::-1] 
        complement={'A':'T','G':'C','C':'G','T':'A','\n':'\n'}
        trantab = str.maketrans(complement)
        rc[key] = re.translate(trantab)
        
        
with open(filename, 'w') as l:
    
    
    _str=""
    for key in seq.keys():            
        _str+=">"+ "%s %d"%(key,length1[key])+ "\n" + "%s"%(rc[key]) + "\n"

    l.writelines(_str)