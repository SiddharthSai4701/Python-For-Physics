# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:04:25 2022

@author: sidvs
"""

import pandas
import matplotlib.pyplot as plt

df1 = pandas.read_table("D:\\College\\6th sem\\UPHY 608\\Epinephrine Data and Codes\\Plot related files\\Epi-Ag1.txt", sep='\s+', skiprows=3)
df1 = df1.rename(columns={"DY/DX":"junk", "Y":"DY/DX", "X":"Y", "#":"X"})
del df1['junk']
ag1_x= df1['X'].iloc[400:2001]
ag1_y= df1['Y'].iloc[400:2001]
plt.plot(ag1_x, ag1_y, label='Ag1')
plt.legend()

df2 = pandas.read_table("D:\\College\\6th sem\\UPHY 608\\Epinephrine Data and Codes\\Plot related files\\Epi-Ag2.txt", sep='\s+', skiprows=3)
df2 = df2.rename(columns={"DY/DX":"junk", "Y":"DY/DX", "X":"Y", "#":"X"})
del df2['junk']
ag2_x= df2['X'].iloc[400:2001]
ag2_y= df2['Y'].iloc[400:2001]
plt.plot(ag2_x, ag2_y, label='Ag2')
plt.legend()

df3 = pandas.read_table("D:\\College\\6th sem\\UPHY 608\\Epinephrine Data and Codes\\Plot related files\\Epi-Ag3.txt", sep='\s+', skiprows=3)
df3 = df3.rename(columns={"DY/DX":"junk", "Y":"DY/DX", "X":"Y", "#":"X"})
del df3['junk']
ag3_x= df3['X'].iloc[400:2001]
ag3_y= df3['Y'].iloc[400:2001]
plt.plot(ag3_x, ag3_y, label='Ag3')
plt.legend()

df4 = pandas.read_table("D:\\College\\6th sem\\UPHY 608\\Epinephrine Data and Codes\\Plot related files\\Epi-Ag4-1.txt", sep='\s+', skiprows=3)
df4 = df4.rename(columns={"DY/DX":"junk", "Y":"DY/DX", "X":"Y", "#":"X"})
del df4['junk']
ag4_x= df4['X'].iloc[400:2001]
ag4_y= df4['Y'].iloc[400:2001]
plt.plot(ag4_x, ag4_y, label='Ag4-1')
plt.legend()