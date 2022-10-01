# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 10:10:40 2021

@author: Siddharth Vijay Sai
"""

import numpy as np
import matplotlib.pyplot as plt


while True:
    n = float(input("Enter a value greater than 1: "))
    if n>1:
        break
    else:
        continue

theta_deg = np.linspace(0,np.pi/2,100)

theta_rad = theta_deg*180/np.pi

term = (pow(n,2)-pow(np.sin(theta_deg),2))**0.5
nsq_cos = pow(n,2)*np.cos(theta_deg)


rte = (np.cos(theta_deg)-term)/(np.cos(theta_deg)+term)
rtm = (-nsq_cos+term)/(nsq_cos+term)

tte = (2*np.cos(theta_deg))/(np.cos(theta_deg)+term)
ttm = ((2*n*np.cos(theta_deg))/(nsq_cos+term))

plt.title("Reflection and Transmission Coefficients\nfor the case of external reflection",fontdict={'fontname':'Impact'})
plt.xlabel("Angle of incidence, $\Theta$ ")
plt.ylabel(("Reflection/Transmission Coefficient"))

plt.xlim(0,90)
plt.ylim(-1.0,1.0)

plt.yticks([-1.0,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1.0])

plt.axhline(y=0.0,color='black')

plt.plot(theta_rad,tte,color='magenta',linestyle='--',label='$t_{TE}$')
plt.plot(theta_rad,ttm,linestyle='--',color='red',linewidth=2,label='$t_{TM}$')
plt.plot(theta_rad,rte,linestyle='-.',color='cyan',linewidth=2,label='$r_{TE}$')
plt.plot(theta_rad,rtm,linestyle='-.',color='orange',linewidth=2,label='$r_{TM}$')


plt.text(60.24,0.682,"$t_{TM}$",bbox=dict(facecolor="red"),alpha=1)
plt.text(52.86,0.520,"$t_{TE}$",bbox=dict(facecolor="magenta"),alpha=1)
plt.text(67.68,-0.451,"$r_{TE}$",bbox=dict(facecolor="cyan"),alpha=1)
plt.text(62.00,0.136,"$r_{TM}$",bbox=dict(facecolor="orange"),alpha=1)

plt.legend()
