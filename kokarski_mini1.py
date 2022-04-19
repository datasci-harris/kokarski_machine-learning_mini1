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

def variablecreation():

    newipums = ipums.assign(EDUCDC=0)
    newipums = newipums.assign(HSDIP=0)
    newipums = newipums.assign(CSDIP=0)
    newipums = newipums.assign(BLACK=0)
    newipums = newipums.assign(WHITE=0)
    newipums = newipums.assign(HISPANIC=0)
    newipums = newipums.assign(MARRIED=0)
    newipums = newipums.assign(FEMALE=0)
    newipums = newipums.assign(VET=0)
    for x in range(0, len(newipums.EDUCDC)):
        # mapping categorical education to continuous using crosswalk dataset
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
        # 1= white, 2= black
        if(newipums.RACE[x] == 1):
            newipums.WHITE[x] = 1
        if(newipums.RACE[x] == 2):
            newipums.BLACK[x] = 2
        # 0 if not hispanic >0 if hispanic
        if(newipums.HISPAN[x] > 0):
            newipums.HISPANIC[x] = 1
        # between 1 and 3 are married (inlcusive)
        if(newipums.MARST[x] >= 1 and newipums.MARST[x] <= 3):
            newipums.MARRIED[x] = 1
        # sex=2 is female
        if(newipums.SEX[x] == 2):
            newipums.FEMALE[x] = 1
        # vet status=2 then they are a vet
        if(newipums.VETSTAT[x] == 2):
            newipums.VET[x] = 1
        # modifying age and incwage
    newipums.AGE = np.square(newipums.AGE)
    newipums.INCWAGE = np.log(newipums.INCWAGE)
    return(newipums)


newdf = variablecreation()
