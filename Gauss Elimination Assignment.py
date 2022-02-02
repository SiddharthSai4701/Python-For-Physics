# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 23:15:00 2022

@author: sidvs
"""
# Importing necessary packages

import numpy as np

# Initializing the arrays

A = np.array([[3,2,-1],
              [2,5,3],
              [-5,2,-1]],dtype=float)
B = np.array([[8,9,0]],dtype=float)
X = np.zeros(3,dtype=float)


# Concatenating the arrays to get them in the reduced row echelon form

M = np.concatenate((A,B.T),axis=1)


# Defining a function to display the elements up to 4 decimal places

def d(A):
    print()
    m = len(A)
    n = len(A[0])
    for i in range(m):
        for j in range(n):
            print("%.4f"%A[i,j],end="\t\t")
        print()

# Displaying the original matrix in reduced row echelon form
    
d(M)  


# Forward Elimination Step
print("\n\n")
print("\t\t\t Forward Elimination")
n = len(M) 
for i in range(n-1):
   # The variable i specifies the pivot row
   
    for j in range(i+1,n):
   # The variable j specifies which row is being modified
   # f is the factor by which the element is multiplied
       f = M[j,i]/M[i,i]
       
       for k in range(n+1):
     # The variable k specifies the column
           M[j,k] = M[j,k] - (f*M[i,k])
           
    # Displaying the modified matrix after each run of the outermost loop      
    d(M)
    
print("\n\n")

# Back Substitution Step
print("\t\t\t Back Substitution")

# Extracting matrices A and B from the matrix M

A = M[:,:-1]
B = M[:,-1]

# Calculating the last element of the solution matrix
X[-1] = B[-1]/A[-1,-1]


# Calculating the sum to use in the formula for back substitution and obtaining the final solution matrix, X

for i in range(n-2,-1,-1):
    s = 0
    for j in range(i+1,n):
        s+= A[i,j]*X[j]
    
    X[i] = (B[i] - s)/A[i,i]
    
# Printing the solution matrix

print("The solution matrix is: ",X,sep="\n")
    