# -*- coding: utf-8 -*-
"""
Created on Sun May  9 12:59:37 2021

@author: bryan
"""

import pandas as pd
import matplotlib.pyplot as plt

# Raw Data to DataFrame
df = pd.read_csv('churn_raw_data.csv', encoding='utf-8')


df.info()
# All rows with null children
df_null_children = df[df['Children'].isnull()]
# All rows with children
df_not_null_children = df[df['Children'].notnull()]

print(df['Population'].unique())