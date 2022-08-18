# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 08:36:49 2022

@author: carme
"""

# import matplotlib.pyplot as plt
# import math as m
from modulos import lectura 

npre, ndia, nmes =lectura.leernike("nike.csv")

preciomax=npre[30] #100%
preciomax=float(preciomax)
precio56=npre[54]
precio56=float(precio56)
porcentajeprecio56=(precio56*100)/preciomax
procenredon=round(porcentajeprecio56,2)
print("Nike cae de 100% el dia 31 a",procenredon,"% el dia 56")
# # areglar con lo del vale

gpre, gdia, gmes =lectura.leernike("google.csv")
preciomaxg=gpre[30] #100%
preciomaxg=float(preciomaxg)
precio56g=gpre[54]
precio56g=float(precio56g)
porcentajeprecio56g=(precio56g*100)/preciomaxg
procenredong=round(porcentajeprecio56g,2)
print("Google cae de 100% el dia 31 a",procenredon,"% el dia 56")
# plt.plot(x,y)
# plt.show()
