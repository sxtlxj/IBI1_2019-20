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

plt.plot(world_date, world_new_cases, 'ro')
plt.plot(world_date, world_new_deaths, "go")
plt.xticks(world_date.iloc[0:len(world_date):4],rotation=-90)


#Question: How have new cases and total cases developed over time in Spain?
rownew = []
rowtotal = []
for i in range(0,7996):
    if covid_data.loc[i,"location"] == "Spain":
        rownew.append(True)
    else:
        rownew.append(False)
spain_new_cases = covid_data.loc[rownew,"new_cases"]

for i in range(0,7996):
    if covid_data.loc[i,"location"] == "Spain":
        rowtotal.append(True)
    else:
        rowtotal.append(False)
spain_total_cases = covid_data.loc[rowtotal,"total_cases"]

for i in range(0,7996):
    if covid_data.loc[i,"location"] == "Spain":
        if covid_data.loc[i,"total_cases"] == 0:
            print("not infected yet:", covid_data.loc[i,"date"])
        else:
            print("infected:", covid_data.loc[i,"date"])

print(spain_new_cases,spain_total_cases)

print(spain_new_cases.describe(),spain_total_cases.describe())
plt.plot(world_date, spain_new_cases, 'b+')
plt.plot(world_date, spain_total_cases, "y+")
plt.xticks(world_date.iloc[0:len(world_date):4],rotation=-90)

