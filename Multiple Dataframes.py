# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 14:22:02 2022

@author: sidvs
"""

import pandas as pd
import os
import matplotlib.pyplot as plt

path = "D:/College/6th sem/UPHY 608/Epinephrine Data and Codes/Plot related files"
files = os.listdir(path)
new_files = []
new_txt_files = []
for i in files:
    if ".xlsx" in i:
        new_files.append(i)
        
    elif ".txt" in i:
        new_txt_files.append(i)
        
for i in new_files:
        df = pd.read_excel(path + "/" + i)
c = ["red","yellow","green","blue","orange"]

for file in new_files:
    df = pd.read_excel(file)
    x = df['X'].iloc[400:2001]
    y = df['Y'].iloc[400:2001]
    plt.subplot(1,2,1)
    plt.plot(x,y,label = file[:-5] )
plt.legend()


for txt_file in new_txt_files:
    df2 = pd.read_csv(path+"/"+txt_file,sep="\s+",skiprows=3)
    df2 = df2.rename(columns = {"DY/DX":"Junk","Y":"DY/DX","X":"Y","#":"X"})
    x = df2['X'].iloc[400:2001]
    y = df2['Y'].iloc[400:2001]
    plt.subplot(1,2,2)
    plt.plot(x,y,label = txt_file[:-4])
plt.legend()
plt.show()