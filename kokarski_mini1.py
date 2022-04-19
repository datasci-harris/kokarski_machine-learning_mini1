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
for x in range(0, len(newipums.EDUCDC)):
    tempeduc = newipums.EDUCD[x]
    temppos = crosswalk[crosswalk["educd"] == tempeduc].index.tolist()[0]
    newipums.EDUCDC[x] = crosswalk.educdc[temppos]
   
   