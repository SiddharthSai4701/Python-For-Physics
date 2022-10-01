# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 21:05:34 2021

@author: Siddharth Vijay Sai
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 23:51:25 2021

@author: sidvs
"""

# Accepting the equation from the user

n = int(input("Enter the order of the polynomial: "))

coeff_list = []
for i in range(n+1):
    coeff_list.append(0)

for i in range(n+1):
    if i>1:
        a = float(input("Enter the coefficient of x^%d: "%(i)))
        coeff_list[len(coeff_list)-1-i] = a
    elif i==1:
        a = float(input("Enter the coefficient of x: "))
        coeff_list[n-1] = a
    elif i ==0:
        a = float(input("Enter the value of the constant: "))
        coeff_list[n] = a

# Printing the equation in standard form

print()
print("\nThe equation is:",end=" ")
for i in range(n,0,-1):
    print( "+ (%f) x^%d "%(coeff_list[len(coeff_list)-1-i],i),end="")        
print("+ (%f)"%coeff_list[n])
print()

# Function to compute the value at a given data point

def f(x):
    l = coeff_list[n]
    #print("l =",l)
    k = 0
    for i in range(n):
        k = k + (coeff_list[i]*pow(x,n-i))
        # print("k =",k)
    return k+l


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
print("----------------------------------------------------------------------------------------------------")
print()
print("====================================================================================================")
print("i \t\t xl \t\t xu \t\t xr \t\t f(xl) \t\tf(xu) \t\tf(xr) \t\tE_approx")
print("====================================================================================================")
# Computing and printing the values of xl, xu and xr and their function values after each iteration

while E_approx>E_threshold:
    
    # Updating the iteration variable
    
    i+=1
    
    # Computing the absolute error
    
    if i>1:
        E_approx = abs((xl-xu)*100/(xl+xu))
    
    
    # Bisection formula
    
    xr = (xl+xu)/2
    
    
    
    print("%d. \t %.6f \t %.6f \t %.6f \t %.6f \t %.6f \t %.6f \t %.6f"%(i,xl,xu,xr,f(xl),f(xu),f(xr),E_approx))
       

    
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
    
    print("----------------------------------------------------------------------------------------------------")
    print()

# Printing the final statement

print("At the end of %d iterations, using Bisection method, we obtained:\n%.6f as the root with an approximate error of %.6f%%" %(i,xr_new,E_approx))
