# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 12:09:54 2021

@author: sidvs
"""
"""
print("This program is a compilation of the 5 programs in this folder!!")

print("Enter your choice:\n")
print("1. Complex Numbers\n")
print("2. Range of Projectile\n")
print("3. Log and Trig functions\n")
print("4. Gravitational Force\n")
print("5. Quadratic Equations\n")

choice=int(input())

if choice==1:
    import math as m

    x = int(input("Enter the real value: "))
    y = int(input("Enter the imaginary value: "))

    import GravitationalForce
    GravitationalForce.comp(x,y)
    """
    
choice=int(input("ENter 1 to say hello"))

if choice==1:
    import Trial
    Trial.hello()
    
elif choice==2:
    import GravitationalForce
    #a = float(input("Enter the mass (in kilograms) of the first object: "))
    #b = float(input("Enter the mass (in kilograms) of the second object: "))
    #c = float(input("Enter the distance (in meters) between the centres of the objects: "))

    print("\nThe value of the Gravitational constant, G is taken to be 6.67430 x 10⁻¹¹ Nm²/kg²")

    G = 6.67430*10**-11

    print("\nThe gravitational force is",GravitationalForce.Gravitational_Force(a,b,c),"N")
    