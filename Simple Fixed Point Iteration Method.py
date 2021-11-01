# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 21:32:30 2021

@author: sidvs
"""

def g(xi):
    return (-2*pow(xi,3) + 11.7*pow(xi,2)+5)/17.7

def f(xi):
    return 2*pow(xi,3) - 11.7*pow(xi,2) + 17.7*xi - 5


xi = float(input("Enter your initial guess: "))

E_thresh = float(input("Enter threshold error: "))
E_approx = 100

i = 0

print()
print("---------------------------------------------------------")
print()
print("=========================================================")
print("i \t\t xi \t\tg(xi) \t\t f(xi) \t\t E_approx")
print("=========================================================")

while E_approx>E_thresh:
    
    

    if i>0:
        f(xi)
        E_approx = abs((xi - x2)/xi)*100
        x2 = xi
        xi = g(xi)
        print("%d. \t %.6f \t %.6f \t  %.6f \t%.6f"%(i,xi,g(xi),f(xi),E_approx))    
        
    
    else:
        print("%d. \t %.6f \t %.6f"%(i,xi,g(xi)))
        x2 = xi
        xi = g(xi)
        
    i+=1
    
    print("---------------------------------------------------------")