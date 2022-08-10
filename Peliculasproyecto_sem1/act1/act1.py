# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 08:51:25 2022

@author: valeb
"""
import random


archi=open('frases_de_peliculas.txt', 'r')
info=archi.readlines()
frases=[]
peliculas=[]


for linea in info:
    linea = linea.rstrip('\n')
    frase, pelicula = linea.split(';')
    frases.append(frase)
    peliculas.append(pelicula)
    # print(frase)
    # print(pelicula)

print("#######################################")
print("#  Películas: Preguntas y respuestas  #")
print("#######################################")
print("Elige una opción")
print("1 - Mostrar lista de películas.")
print("2 - ¡Trivia de película!")
print("3 - Mostrar secuencia de opciones seleccionadas previamente.")
print("4 - Borrar historial de opciones.")
print("5 - Salir")
opcion = int(input())

peli_ordenadasalf = sorted(peliculas)

pelis_final=[]
for n in range(len(peli_ordenadasalf)):
    num=str(n+1)
    linea= num + '- ' +peli_ordenadasalf[n]
    pelis_final.append(linea)
    

if opcion == 1:
    for n in (pelis_final):
        print(n)
#listo la 1

pelis_random = []
pelisrandom = random.shuffle(pelis_final)
print(pelisrandom)







    

