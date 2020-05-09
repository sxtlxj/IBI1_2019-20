# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 13:43:09 2020

@author: DM
"""
#input the sequence
seq = 'ATGCGACTACGATCGAGGGCCAT'
re = seq[::-1] #reverse the sequence
#create a dictionary to make a complementary sequence
complement = {'A':'T', 'G':'C', 'T':'A', 'C':'G' }

trantab = str.maketrans(complement)
rc = re.translate(trantab)
print(rc)