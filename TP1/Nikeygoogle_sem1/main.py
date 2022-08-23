# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 08:40:11 2022

@author: valeb
"""

import modulos.lectura_archivos
import modulos.analisis
import modulos.graficacion as graf


fechas_nike, precios_nike = modulos.lectura_archivos.leer_nike('nike.csv')

fechas_google, precios_google = modulos.lectura_archivos.leer_google('google.csv')


porcentaje_1 = modulos.analisis.pregunta_1(fechas_google, precios_google)
print("El porcentaje de caida entre la semana 31 y 56 es de:",porcentaje_1,"%")
#respuesta pregunta 1


print("Sii, tiene sentido, ya que se trata de un porcentaje negativo(caida), y en el grafico se ve que cae de 10 a -20 (30% de caida aprox)")


porcentaje_3 = modulos.analisis.pregunta_3(fechas_google, precios_google)
print(porcentaje_3)
print("Si, tambien tiene sentido")

nike_norm_x, nike_norm_y = modulos.analisis.datos_norm(precios_nike)
google_norm_x, google_norm_y = modulos.analisis.datos_norm(precios_google)


graf.graficar_norm(nike_norm_x, nike_norm_y, google_norm_x, google_norm_y)
#grafica normalizada de ambas empresas

nike_porc_x, nike_porc_y = modulos.analisis.datos_porc(precios_nike)
google_porc_x, google_porc_y = modulos.analisis.datos_porc(precios_google)

graf.graficar_porc(nike_porc_x, nike_porc_y, google_porc_x, google_porc_y)

graf.graficar_todo(nike_norm_x, nike_norm_y, google_norm_x, google_norm_y, nike_porc_x, nike_porc_y, google_porc_x, google_porc_y)






