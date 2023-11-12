# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 14:45:14 2022

@author: sidvs
"""

import random as r
import numpy as np
import matplotlib.pyplot as plt

r.seed()

n = int(input("Number of points to consider: "))
X = np.zeros(n)
Y = np.zeros(n)

count = 0

for i in range(n):
    X[i],Y[i] = r.random(),r.random()
    
    if (pow(X[i],2) + pow(Y[i],2))<=1:
        count+=1

print("The value of \u03C0 is: ",count*4/n)
        
x = np.linspace(0,1,1000)
y = np.sqrt(1-pow(x,2))

plt.plot(x,y,color='red',linewidth=3)
plt.scatter(X,Y,c='green',alpha=0.5)