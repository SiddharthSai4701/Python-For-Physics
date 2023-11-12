# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:58:05 2022

@author: sidvs
"""

import matplotlib.pyplot as plt
import numpy as np
import math as m
import scipy.stats as stat
from matplotlib.patches import Polygon

N=100
X = np.random.random(N)

a = 0
bins = 10
o_i = np.zeros(bins)

for i in range(bins):
    
    b=a+0.1
    for j in range(N):
        
        if X[j]>=a and X[j]<b:
            o_i[i]+=1
    a+=0.1

print("\nThe distribution of", bins,"bins are: ",o_i)

chi_sq_c = 0
expected = N/bins

for i in range(bins):
    chi_sq_c+=((o_i[i]-expected)**2)/expected

print("\nValue of the Chi_Sq_C: ",chi_sq_c)

c,p=stat.chisquare(o_i)
print("c=", c,", p=",p)

x = np.linspace(0.1, 20, 1000)
k = bins-1
prob_density = (0.5**(k/2))*(x**((k/2)-1))*np.exp(-x/2)/m.gamma(k/2)
plt.plot(x, prob_density, label="k="+str(k))

shade_x = np.linspace(c, 20, 1000)
shade_prob_density = (0.5**(k/2))*(shade_x**((k/2)-1))*np.exp(-shade_x/2)/m.gamma(k/2)
ax = plt.gca()
verts=[(c,0), *zip(shade_x, shade_prob_density), (20,0)]
polygon = Polygon(verts, facecolor="0.75", edgecolor="0.75")
ax.add_patch(polygon)

plt.legend()