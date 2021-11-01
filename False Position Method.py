# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 14:08:03 2021

@author: sidvs
"""

"""

   * * * False Position Method  * * *

A parachutist free falls for t = 10s with g = 9.8 m/s. He attains a velocity of
40 m/s. If his mass is 68 kg, determine the drag coefficient 'c' using the
equation:
    
    v = (gm(1-e^(-ct/m)))/c
"""

# Importing the necessary libraries and initialising the variables

from math import *

t = 10
v = 40
g = 9.8  
m = 68.1

# Function to calculate the values at the specified points

def f(c):
    return v - (g*m/c)*(1-exp(-c*t/m))

# Accepting the two guesses from the user

while True:
    xl = float(input("Enter the value of xl: "))
    xu = float(input("Enter the value of xu: "))
    
    if f(xl)*f(xu)<0:
        break
    else:
        print("Try again!")
        continue        
    
# Initialising the loop  variable to 0, approximate error to 100%, accepting the threshold error from the user

E_approx = 100
E_threshold = float(input("Enter the threshold error: "))
i = 0

print()
print("----------------------------------------------------------------------------------------------------------")
print()
print("====================================================================================================")
print("i \t\t xl \t\t xu \t\t xr \t\t f(xl) \t\tf(xu) \t\tf(xr) \t\tE_approx")
print("====================================================================================================")

# Computing and printing the values of xl, xu and xr and their function values after each iteration

while E_approx>E_threshold:
    
    # Updating the iteration variable
    
    i+=1
    
    # False Position formula
    
    xr = xu - ((f(xu)*(xl-xu))/(f(xl)-f(xu))) 
    
    print("%d. \t %.6f \t %.6f \t %.6f \t %.6f \t %.6f \t %.6f \t %.6f"%(i,xl,xu,xr,f(xl),f(xu),f(xr),E_approx))
    
    # Computing the absolute error
    
    if i>1:
        E_approx = abs((xr_new-xr)*100/xr_new)
    
    # Updating xu and xl
    
    if f(xl)*f(xr)<0:
        xu = xr
        
    elif f(xu)*f(xr)<0:
        xl = xr
    else:
        print(xr,"is the root")
        break
        
    # Updating xr
    
    xr_new = xr
    
    print("----------------------------------------------------------------------------------------------------------")    
    print()
    
# Printing the final statement
    
print("At the end of %d iterations, using False Position method, we obtained:\n%.6f as the root with an approximate error of %.6f%%" %(i,xr_new,E_approx))