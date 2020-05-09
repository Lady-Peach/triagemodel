# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:09:38 2020

@author: lyatt
"""

import pandas as pd
TextData = pd.read_csv (r'C:\Users\lyatt\Documents\JCU\12. Project 2\ED_Patients_Data.csv', usecols = [0, 5, 8, 9])
TextDataSubset = TextData.sample(n = 500)
print(TextDataSubset.head())
#Take a look at whats in the text for the simple variable in the subset
TextDataSubset['PRESENTING_PROBLEM'].value_counts()
#I wonder what will happen if I do this to the Triage Presenting information data?
TextDataSubset['TRIAGE_PRESENTING_INFORMATION'].value_counts() #Thats very interesting
#Create the key variabl
TextDataSubset['UNIQUE_IDENTIFIER'] = TextDataSubset['PATIENT_ID']+ TextDataSubset['TRIAGE_DT_TM']
#Set the index to our new unique identifier
TextDataSubset = TextDataSubset.set_index('UNIQUE_IDENTIFIER')
