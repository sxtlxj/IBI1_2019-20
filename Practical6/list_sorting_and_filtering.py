# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:49:48 2020

@author: DM
"""

import matplotlib.pyplot as plt #import plt to make boxplot

gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
maximum = max(gene_lengths) # get the maximum and minimum in the gen_lengths
minimum = min(gene_lengths)

deletion = [maximum,minimum]
gene_lengths.remove(maximum)
gene_lengths.remove(minimum)
gene_lengths.sort() # sort the remaining genes
print(gene_lengths)


plt.boxplot(gene_lengths, vert = True, 
            whis =1.5, patch_artist = True, 
            meanline = False, showbox = True, 
            showcaps = True, showfliers = True, notch =False)
plt.show()
                    
