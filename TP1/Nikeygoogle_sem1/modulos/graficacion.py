# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 08:39:57 2022

@author: valeb
"""
import matplotlib.pyplot as plt


def graficar_norm(n_norm_x, n_norm_y, g_norm_x, g_norm_y):
    
    plt.plot(n_norm_x, n_norm_y, color="black", label="Nike")
    plt.plot(g_norm_x, g_norm_y, color="r", label= "Google")
    plt.legend(loc="lower right",fontsize=12)
    
    plt.grid()
    plt.show()
    

  
    
def graficar_porc(n_porc_x, n_porc_y, g_porc_x, g_porc_y):
    
    plt.plot(n_porc_x, n_porc_y, color="b", label= "Nike")
    plt.plot(g_porc_x, g_porc_y, color="y", label= "Google")
    plt.legend(loc="lower right", fontsize=12)
    
    plt.grid()
    plt.show()
    
def graficar_todo(n_norm_x, n_norm_y, g_norm_x, g_norm_y, n_porc_x, n_porc_y, g_porc_x, g_porc_y):
    
    fig, (ax1, ax2) = plt.subplots(nrows=1,ncols=2,figsize=(15,8))
    
    ax1.plot(n_norm_x, n_norm_y, color="black", label="Nike")
    ax1.plot(g_norm_x, g_norm_y, color="r", label= "Google")
    ax1.legend(loc="lower right",fontsize=12)
    ax1.grid()
    
    ax2.plot(n_porc_x, n_porc_y, color="b", label= "Nike")
    ax2.plot(g_porc_x, g_porc_y, color="y", label= "Google")
    ax2.legend(loc="lower right", fontsize=12)
    ax2.grid()
    
    fig.supxlabel("Evolución del precio de Google y Nike. Normalizado en por unidad (izq.) y tasa de crecimiento respecto al precio de inicial (der.) del año 2020")
    
    plt.show()