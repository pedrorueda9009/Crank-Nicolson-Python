# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 18:57:57 2021

@author: Pedro Rueda

Para aplicar el método de Cranck-Nicolson 1d para ecuaciones de la forma:
    
    dT / dt  =  k * (d**2)T / dx**2
    
necesitamos ingresarle la función f = T
en su momento inicial, las condiciones de frontera borde 1 = b1, y borde 2 = b2.
el parametro k, dt, dx, Nx es la cantidad de nodos internos

"""
import numpy as np
import LU_deco as LU

def crank_nicolson1d(f,b1,b2,k,dt,t,dx,Nx):
    
    lam = k*dt / (dx**2) 
    
    tiempo = 0 
    while(tiempo < t):
    
        # Creacion de Matriz A
        matriz = 2*(1+lam)*np.identity(Nx,float) - lam*np.eye(Nx,k=-1) - lam*np.eye(Nx,k=1)
            
        # Creacion de Matriz b
        b = np.zeros([Nx,1])    
        
        for i in range(Nx):
            # llenamos el primer elemento
            if (i == 0):
                b[0] = 2*lam*f[0] + 2*(1-lam)*f[1] + lam*f[2]
                continue
            if (i == Nx-1):
                b[Nx-1] = 2*lam*f[Nx+1] + 2*(1-lam)*f[Nx] + lam*f[Nx-1]
                continue
            else:
                b[i] = lam*f[i] + 2*(1-lam)*f[i+1] + lam*f[i+2]
        
        # aplicamos reduccion LU
        sol = LU.LU_deco(matriz, b)
        
        for i in range(4):
            f[i+1] = round(float(sol[i]),5)
            
        tiempo = tiempo + dt
    
    return f
    