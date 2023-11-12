# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:03:32 2022

@author: sidvs
"""

import pandas
import matplotlib.pyplot as plt

df_1 = pandas.read_excel(r"D:\\College\\6th sem\\UPHY 608\\Epinephrine Data and Codes\\Plot related files\\Epi_1mM.xlsx")
df_1_X = df_1['X']
df_1_Y = df_1['Y']
plt.plot(df_1_X, df_1_Y, label="Epi_1mM")
plt.legend()

df_2 = pandas.read_excel(r"D:\\College\\6th sem\\UPHY 608\\Epinephrine Data and Codes\\Plot related files\\Epi_10mM.xlsx")
df_2_X = df_2['X']
df_2_Y = df_2['Y']
plt.plot(df_2_X, df_2_Y, label="Epi_10mM")
plt.legend()

df_3 = pandas.read_excel(r"D:\College\6th sem\UPHY 608\Epinephrine Data and Codes\Plot related files\Epi_10uM.xlsx")
df_3_X = df_3['X']
df_3_Y = df_3['Y']
plt.plot(df_3_X, df_3_Y, label="Epi_10uM")
plt.legend()

df_4 = pandas.read_excel(r"D:\College\6th sem\UPHY 608\Epinephrine Data and Codes\Plot related files\Epi_100uM.xlsx")
df_4_X = df_4['X']
df_4_Y = df_4['Y']
plt.plot(df_4_X, df_4_Y, label="Epi_100uM")
plt.legend()