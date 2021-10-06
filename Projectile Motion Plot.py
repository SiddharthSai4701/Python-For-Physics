# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:11:38 2021

@author: sidvs
"""

import numpy as np
import matplotlib.pyplot as plt

velocity = float(input("Enter the velocity in ms⁻¹: "))
angle = float(input("Enter the angle in degrees: "))
k = float(input("Enter the value of the drag coefficient: "))

U = velocity*np.cos(angle)
V = velocity*np.sin(angle)
g = 9.8
T = 2*V/g
t = np.linspace(0,T,500)

# Without Resistance

x = U*t
y = V*t - 0.5*g*pow(t,2)

plt.plot(x,y,'r--',label="Without Resistance")


# With Resistance

xr =  (U/k)*(1-np.exp(-k*t))
yr = (-g*t/k) + (((k*V+g)*(1-np.exp(-k*t)))/pow(k,2))

plt.plot(xr,yr,'b-.',label="With Resistance")

plt.title("Projectile Motion")
plt.xlabel("Horizontal distance (in m)")
plt.ylabel("Vertical distance (in m)")
plt.legend()