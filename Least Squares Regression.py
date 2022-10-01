# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 18:06:15 2021

@author: Siddharth Vijay Sai
"""

import numpy as np
import matplotlib.pyplot as plt

x = [8,2,11,6,5,4,12,9,6,1]
y = [3,10,3,6,8,12,1,4,9,14]

# To calculate the respective columns

xi = np.array(x)
yi = np.array(y)
xi_squared = pow(xi,2)
yi_squared = pow(yi,2)
xiyi = xi*yi
n = len(xi)

sum_xi = sum(xi)
sum_yi = sum(yi)
sum_xi_squared = sum(xi_squared)
sum_yi_squared = sum(yi_squared)
sum_xiyi = sum(xiyi)

# To calculate a1 and a0

numerator = (n*sum_xiyi) - (sum_xi*sum_yi)
denominator = (n*sum_xi_squared) - pow(sum_xi,2)

a1 = numerator/denominator
a0 = (sum_yi/n) - (a1*sum_xi/n)

# To calculate r and r squared

r_denominator = pow((n*sum_xi_squared) - pow(sum_xi,2),0.5)*pow((n*sum_yi_squared) - pow(sum_yi,2),0.5)

r = numerator/r_denominator

print("Equation of the best fit line is: ")
print("y = %.6f x + %.6f"%(a1,a0))
print("\n It has an r^2 value of %.6f"%(r**2))

# Y line

y_line = a1*xi + a0

# Plotting the graph

plt.scatter(xi,yi,label='Data Points',c='r')
plt.plot(x,y_line,':g',label='Line of Best Fit')
plt.title("Least Squares Regression")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xticks(x)
plt.yticks(y)
plt.text(2,1,"y = %.6f x + %.6f\n $r^2$ = %.4f"%(a1,a0,r**2),bbox=dict(facecolor="cyan"),alpha=1)
plt.plot()
plt.legend(loc="best")
