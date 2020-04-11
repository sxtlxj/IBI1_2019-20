# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:44:50 2020

@author: DM
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("D:\computer\IBI1_2019-20\Practical7")
covid_data = pd.read_csv("full_data.csv")
my_columns = [True, True, False, True, False,False]
print(covid_data.iloc[:,0:15:3])

my_rows = []
for i in range(0,7996):
    if covid_data.loc[i,"location"] == "Afghanistan":
        my_rows.append(True)
    else:
        my_rows.append(False)
Afghanistan = covid_data.loc[my_rows,"total_cases"]
print(Afghanistan)

my_rows1 = []
my_rows2 = []
my_rows3 = []
for i in range(0,7996):
    if covid_data.loc[i,"location"] == "World":
        my_rows1.append(True)
    else:
        my_rows1.append(False)
world_new_cases = covid_data.loc[my_rows1,"new_cases"]

for i in range(0,7996):
    if covid_data.loc[i,"location"] == "World":
        my_rows2.append(True)
    else:
        my_rows2.append(False)

for i in range(0,7996):
    if covid_data.loc[i,"location"] == "World":
        my_rows3.append(True)
    else:
        my_rows3.append(False)
world_new_deaths = covid_data.loc[my_rows1,"new_deaths"]

world_date = covid_data.loc[my_rows1,"date"]

print(world_new_cases,world_date)
median = world_new_cases.median()
mean = world_new_cases.mean()
print(median,"\n",mean)


plt.plot(world_date, world_new_cases, 'r+')
plt.plot(world_date, world_new_deaths, "y+")
plt.xticks(world_date.iloc[0:len(world_date):4],rotation=-90)

