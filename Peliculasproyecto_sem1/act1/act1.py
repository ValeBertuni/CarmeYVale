# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 08:51:25 2022

@author: valeb
"""

archi=open('frases_de_peliculas.txt', 'r')
info=archi.readlines()

for linea in info:
    frase, pelicula = linea.split(';')
    print(frase)
    print(pelicula)