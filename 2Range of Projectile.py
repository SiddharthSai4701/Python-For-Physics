# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 15:14:27 2021

@author: sidvs
"""
import math as m

velocity = float(input("Enter the velocity in ms⁻¹: "))
angle = float(input("Enter the angle in degrees: "))

angle = angle*3.14/180
def range_of_projectile(velocity,angle):
    R = ((m.pow(velocity,2)*m.sin(2*angle))/9.8)
    
    return R

print("The range of the projectile is",range_of_projectile(velocity, angle),"m")