# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:35:10 2021

@author: Siddharth Vijay Sai
"""

import math as m

x = int(input("Enter the real value: "))
y = int(input("Enter the imaginary value: "))


def comp(x=0,y=0):
    print("The complex number is",complex(x,y))   # The complex number
    print("The complex conjugate is",complex(x,-y)) # The conjugate of the complex number
    print("The modulus is",int(m.pow((x**2+y**2),0.5))) # The modulus of the complex number
    print("The argument is",m.atan(y/x)) # The argument of the complex number
    
comp(x,y)
