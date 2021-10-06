# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 15:19:32 2021

@author: sidvs
"""
import math
g = 9.8 #m/s2
def velocity(mass=68.1,time=10,drag=14.7942):
    return ((g*mass)*(1-math.exp(-(drag/mass)*time)))/drag
print(velocity(time=30,mass=50,drag=15))