# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 13:43:09 2020

@author: DM
"""

seq = 'ATGCGACTACGATCGAGGGCCAT'
re = seq[::-1]

d = {'A':'T', 'G':'C', 'T':'A', 'C':'G' }

trantab = str.maketrans(d)
rc = re.translate(trantab)
print(rc)