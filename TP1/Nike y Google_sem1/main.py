# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 08:36:49 2022

@author: carme
"""

# import matplotlib.pyplot as plt
# import math as m
import modulos

# archi=open("nike.csv", "r")
# for i in range(1):
#     aux=archi.readline()
# entero=archi.readlines()
# nikefecha=[];nikepre=[];nikedia=[];nikemes=[]; nikeanioyhora=[]
# for linea in entero:
#     nikef, nikep=linea.split(',')
#     nikefecha.append(nikef)
#     nikepre.append(nikep)
# for lin in nikefecha:
#     niked, nikem, nikeayh=lin.split('/')
#     nikedia.append(niked)
#     nikemes.append(nikem)
#     nikeanioyhora.append(nikeayh)

nikep=modulos.lectura.leernike("nike.csv")
print("lista de precio:",nikep)
# preciomax=nikepre[30] #100%
# preciomax=float(preciomax)
# precio56=nikepre[54]
# precio56=float(precio56)
# porcentajeprecio56=(precio56*100)/preciomax
# procenredon=round(porcentajeprecio56,2)
# print("Nike cae de 100% el dia 31 a",procenredon,"% el dia 56")
# # areglar con lo del vale


# plt.plot(x,y)
# plt.show()
