#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 21:21:09 2022

@author: kaylaokarski
"""

import pandas as pd
import numpy as np

#import dataset
ipums = pd.read_csv("Documents/GitHub/kokarski_machine-learning_mini1/usa_00003.csv")
crosswalk = pd.read_csv("Documents/GitHub/kokarski_machine-learning_mini1/PPHA_30545_MP01-Crosswalk.csv")

# (2) variable creation (a)
# mapping categorical education variable to continuous using crosswalk dataset
newipums = ipums.assign(EDUCDC=0)
newipums = newipums.assign(HSDIP=0)
newipums = newipums.assign(CSDIP=0)

for x in range(0, len(newipums.EDUCDC)):
    tempeduc = newipums.EDUCD[x]
    temppos = crosswalk[crosswalk["educd"] == tempeduc].index.tolist()[0]
    newipums.EDUCDC[x] = crosswalk.educdc[temppos]
   
# creating dummy variables:
# hsdip (063 or 063)
    if(newipums.EDUCD[x] == 63 or newipums.EDUCD[x] == 64):
        newipums.HSDIP[x] = 1
# csdip 101 and 116 (inclusive)
    if(newipums.EDUCD[x] >= 101 and newipums.EDUCD[x] <= 116):
        newipums.CSDIP[x] = 1