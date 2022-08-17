# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 09:19:57 2022

@author: carme
"""
import random

frases=[]
peliculas=[]

archi=open('frases_de_peliculas.txt', 'r')
info=archi.readlines()
for linea in info:
    linea=linea.rstrip("\n")
    frase, pelicula= linea.split(';')
    frases.append(frase)
    peliculas.append(pelicula)
    
pelisordenadas=sorted(peliculas)

pelisfinal1=[]
pelisxshufle=[]
for i in range (len(pelisordenadas)):
    ind=str(i+1)
    linea=ind+"-"+pelisordenadas[i]
    pelisfinal1.append(linea)
for i in range (len(pelisordenadas)):
    ind=str(i+1)
    linea=ind+"-"+pelisordenadas[i]
    pelisxshufle.append(linea)
    
#2 se debe seleccionar una frase al azar y ofrecer una lista de tres películas
#diferentes a la que podría pertenecer la frase. Si acierta, se le debe 
#felicitar. Si falla, se le debe informar.

random.shuffle(pelisxshufle)
    
    
op=int(input("Ingrese su opcion:"))
if op==1:
    for n in (pelisfinal1):
        print(n)
elif op==2:
    print(pelisxshufle)
    pass
elif op==3:
    pass
elif op==4:
    pass
elif op==5:
    pass