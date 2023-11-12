# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:05:05 2022

@author: sidvs
"""

import matplotlib.pyplot as plt
import numpy
import math

x = numpy.linspace(0.1, 20, 1000)

for k in range (1, 10):
    
    chi_sqr_dist = (0.5**(k/2))*(x**((k/2)-1))*numpy.exp(-x/2)/math.gamma(k/2)
    plt.plot(x, chi_sqr_dist, label="k="+str(k))

plt.legend()
plt.show()