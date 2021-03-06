# -*- coding: utf-8 -*-
"""
Created on Wed May 13 19:28:01 2020

@author: DM
"""

import xml.dom.minidom
import pandas as pd
import re

df = pd.DataFrame(columns=['id','name','definition','childnodes']) # create the data frame

DOMTree=xml.dom.minidom.parse("go_obo.xml") #parse the xml file
collection=DOMTree.documentElement
terms = collection.getElementsByTagName("term")     

def CountChild(x):
    '''
    count the number of childnodes of a given element x
    '''
    counter=0
    xid=x.getElementsByTagName('id')[0].childNodes[0].data
    for y in terms:
        if y.getElementsByTagName("is_a"): 
            for i in range(len(y.getElementsByTagName("is_a"))):  #there can be more than <is_a> elements of one GO              
                is_a=y.getElementsByTagName('is_a')[i].childNodes[0].data
                if is_a==xid:
                    counter+=1+CountChild(y)   #use recursion to find all childnodes             
    return counter 
        


for a in terms:
    defstr=a.getElementsByTagName('defstr')[0].childNodes[0].data
    if re.search('autophagosome',defstr): #search GOs that are related to autophagosome
        definition=a.getElementsByTagName('defstr')[0].childNodes[0].data
        ID=a.getElementsByTagName('id')[0].childNodes[0].data
        name=a.getElementsByTagName('name')[0].childNodes[0].data
        childnodes=CountChild(a)
        line={'id':ID,'name':name,'definition':definition,'childnodes':childnodes} #add the information of selected GO to data frame
        df = df.append(line,ignore_index=True)

df.to_excel("autophagosome.xlsx",index=False) #change data frame to excel
        
                         



