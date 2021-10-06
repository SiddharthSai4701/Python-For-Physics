# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 12:27:24 2021

@author: "sidvs"
"""

"""
Write a program to calculate the roots of a quadratic equation. Use the -B +- .... Formula.

Requirements of the program....
1. You must ask the user for entering the coefficients A,B,C....

2. You must pass the coefficients to a function and calculate the roots within the function. The function must return the two roots. You have to receive these two roots outside the function and then print them


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

print("The roots of the equation are:",quad_solution(n1,n2,n3))

