# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:37:18 2020

@author: DM
"""

a = 123
b = 123123
c = b/7
print(b%7)
print(c)
d=c/11
e=d/13
print(d,e)
if e>a:
    print('e>a')
elif e<a:
    print('e<a')
else:
    print('e=a')

x= 1>2
y = 1<2
print(x,y)
z= x and not y or y and not x
print(z)
w = x!=y
z == w