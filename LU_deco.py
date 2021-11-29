# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 17:05:48 2021

@author: Pedro Rueda
Metodo Numerico descomposicion LU para matrices cuadradas NxN
"""


import numpy as np

def LU_deco(A,b):
    
    n = len(A)
    # fase de descomposicion / reduccion de gauss con algunos cambios
        
    for k in range(n-1):
        for i in range(k+1,n):
            
            factor = A[i,k] / A[k,k]
            A[i,k] = factor
                    
            for j in range(k+1,n):
                A[i,j] = A[i,j] - factor * A[k,j]
                    
            
    # fase de substitucion 
    #     forward substitution / algoritmo de descenso
    for i in range(1,n):
        sum = b[i]
        for j in range(i):
            sum = sum - A[i,j]*b[j]
            
        b[i] = sum
    
    #     backward substitution / algoritmo de remonte
    
    x = np.zeros([n,1])
    
    x[n-1] = b[n-1] / A[n-1,n-1]
    
    ii = np.linspace(n-2,0,n-1)
    for i in ii:
        i = int(i)
        for j in range(i,n):
            x[i] = x[i] - A[i,j]*x[j] 
                
        x[i] = x[i] + b[i]
        x[i] = x[i] / A[i,i]
            
    return x




# A = np.array([[3,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,10]])
# b = np.array([[7.85],[-19.3],[71.4]])


# x = LU_deco(A,b)
# print(x)


    