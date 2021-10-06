# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 15:30:20 2021

@author: sidvs
"""

import math as m

num = float(input("Enter a number: "))

def math_funcs(num):
    
    print("the log of",num,"is",m.log10(num))
    print("The square of",num,"is",m.pow(num,2))
    print("The sine of",num,"is",m.sin(num))
    print("The cosine of",num,"is",m.cos(num))
    
    
math_funcs(num)
