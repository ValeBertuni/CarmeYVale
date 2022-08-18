# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 08:39:36 2022

@author: valeb
"""


def leer_nike(csv_nike):
    fechas = []
    precios = []
    
    archi=open('nike.csv')
    infobasura = archi.readline() #lectura primera linea basura
    
    info = archi.readlines()
    for linea in info:
        linea = linea.rstrip()
        fechaaux, precio = linea.split(',')
        fecha, hora = fechaaux.split(' ')
        precio = float(precio)
        precios.append(precio)
        fechas.append(fecha)
    
    return fechas, precios

def leer_google(csv_google): 
    fechas = []
    precios = []
    
    archi=open('google.csv')
    infobasura = archi.readline() #lectura primera linea basura
    
    info = archi.readlines()
    for linea in info:
        linea = linea.rstrip()
        fechaaux, precio = linea.split(',')
        fecha = fechaaux
        precio = float(precio)
        precios.append(precio)
        fechas.append(fecha)
    
    return fechas, precios
    
    