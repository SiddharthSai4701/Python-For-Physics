# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 15:39:00 2021

@author: sidvs
"""

a = float(input("Enter the mass (in kilograms) of the first object: "))
b = float(input("Enter the mass (in kilograms) of the second object: "))
c = float(input("Enter the distance (in meters) between the centres of the objects: "))

print("\nThe value of the Gravitational constant, G is taken to be 6.67430 x 10⁻¹¹ Nm²/kg²")

G = 6.67430*10**-11

def Gravitational_Force(m1,m2,r):
    F = (G*m1*m2)/r**2
    return F

print("\nThe gravitational force is",Gravitational_Force(m1=a,m2=b,r=c),"N")