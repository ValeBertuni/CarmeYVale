# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 11:09:35 2022

@author: valeb
"""
import random

def preguntar(numeroopcion):
    numero=0
    numeroopcion=int(input("Quiere elegir otra opcion? (ingrese 1,2,3,4,5, o otro si no quiere): "))
    if numeroopcion==2:
        numero=2
    elif numeroopcion==3:
        numero=3 
    elif numeroopcion==4:
        numero=4
    elif numeroopcion==5:
        numero=5 

    return numero


def pregunta_1(pelis_y_frases):
    lista = []
    for linea in pelis_y_frases:
        index, peli, frase = linea.split("/")
        linea1 = index + peli
        linea1 = linea.lstrip()
        lista.append(linea1)
    return lista

def pregunta_2(lista_peliculas):
    random.shuffle(lista_peliculas)
    pelis=[]
    frases=[]
    for pelicula in lista_peliculas:
        index, peli, frase = pelicula.split('/')
        pelis.append(peli)
        frases.append(frase)
    print("Su frase es: ",frases[0])
    print("Usted debera elegir escribiendo el numero de las siguientes opciones: ")
    opciones = [pelis[0],pelis[1],pelis[2]]
    random.shuffle(opciones)
    for i in range(len(opciones)):
        linea = str(i) + '-' + opciones[i]
        print(linea)
    n=int(input('Su opcion es: '))
    if pelis.index(opciones[n]) == frases.index(frases[0]):
        print('Grande')
    else:
        print('Proba de nuevo :(')
        
    
    
    
    
