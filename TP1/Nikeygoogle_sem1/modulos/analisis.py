# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 08:39:48 2022

@author: valeb
"""

def pregunta_1(fechas_google, precios_google):
    
    precio_sem31 = precios_google[29]
    precio_sem56 = precios_google[54]
    
    porcentaje = ((precio_sem56-precio_sem31)/precio_sem31)*100
    
    return porcentaje


def pregunta_3(fechas_google, precios_google):
    
    precio_soporte = precios_google[54]
    precio_ultimo = precios_google[len(precios_google)-1]
    
    porcentaje = ((precio_ultimo-precio_soporte)/precio_soporte)*100
    
    return porcentaje