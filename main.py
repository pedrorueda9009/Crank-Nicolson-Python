# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import crank_nicolson as CN


                    # Metodo de Crank-Nicolson en geometria planar en 1d por defecto
                    # def crank_nicolson(f,d=1):
                    #     print("hola")

                    # pi = 3.14159265359                  # numero pi
                    # n0 = 1.33                           # indice de refraccion del agua pura
                    # w0 = 1                              # ancho del haz
                    # f0 = 0.3                            # distancia de foco en metros
                    # lam0 = 820e-9                       # longitud de onda central en metros
                    # k0 = n0*2*pi / lam0                 # numero de onda central
                    
                    # xmax = 1.5e-3 
                    # Nx = 100
                    # x = np.linspace(-xmax,xmax,Nx)      # arreglo espacial
                    # dx = x[1]-x[0]                      # paso espacial en grilla
                    # puntosZ = 1000                      # metros
                    # z = np.linspace(0,10,puntosZ)
                    # dz = z[1]-z[0]
                    # delta = dz / (4*k0*(dx**2))



x = [0,2,4,6,8,10]
dx = 2
Nx = len(x) - 2 # defino los nodos internos del alambre
k = 0.835           # cm2 / seg
dt = 0.1           # tiempo en segundos
t = 0.2
f = [100,0,0,0,0,50]

# condiciones de frontera
b1 = f[0]
b2 = f[len(x)-1]

# Aolicando el metodo de Crank-Nicolson
sol = CN.crank_nicolson1d(f, b1, b2, k,dt,t, dx, Nx)


# el resultado me está indicando la temperatura final de la barra cuando ah pasado t tiempo. 
print(sol)