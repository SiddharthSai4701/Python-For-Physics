# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 15:57:03 2021

@author: sidvs
"""

import math as m

print("This program calculates the roots of a quadratic equation ")

n1 = int(input("Enter the value of the coefficient of x\u00b2: "))
n2 = int(input("Enter the value of the coefficient of x: "))
n3 = int(input("Enter the value of the constant: "))


def quad_solution(a,b,c):
    r1 = (-b + m.sqrt(b**2 -4*a*c))/2*a
    r2 = (-b - m.sqrt(b**2 -4*a*c))/2*a
    
    return r1,r2

print("The roots of the equation are:",quad_solution(a=n1,b=n2,c=n3))