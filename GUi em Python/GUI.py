#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 07:50:01 2019

@author: eduardo
"""
# =============================================================================
#
#                  TODOS OS IMPORTS UTILIZADOS NO SISTEMA
#
# =============================================================================
import matplotlib
import numpy
import sys
import math

import tkinter

import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Se tiver alguma janela aberta, feche todas antes de executar o programa.
#close("all")


# Cria a janelaFigureCanvasTkAgg
root  = tkinter.Tk()

def printa():
    # Vetor de Alpha.
    # ---------------
    vetor_alpha = [flag_alpha_menos_9.get(), 
                   flag_alpha_menos_6.get(),
                   flag_alpha_menos_3.get(),
                   flag_alpha_zero.get(),
                   flag_alpha_mais_3.get(),
                   flag_alpha_mais_6.get(),
                   flag_alpha_mais_9.get()]
    
    # Vetor de Beta.
    # ---------------
    vetor_beta  = [flag_beta_zero.get(), 
                   flag_beta_mais_3.get(),
                   flag_beta_mais_6.get()]
    
    # Vetor de Mach.
    # --------------
    vetor_mach  = [flag_mach_05.get()] 
    
    
    # Contador de variáveis.
    # ----------------------
    cont_alpha = 0
    cont_beta  = 0
    cont_mach  = 0
    index_alpha = []
    index_beta  = []
    index_mach  = []
    
    for i in range(7):
        if (vetor_alpha[i] == 1):
            cont_alpha = (cont_alpha + 1)
            index_alpha.append(i)
    
    for i in range(3):
        if (vetor_beta[i] == 1):
            cont_beta = (cont_beta + 1)
            index_beta.append(i)
            
    for i in range(1):
        if (vetor_mach[i] == 1):
            cont_mach = (cont_mach + 1)
            index_mach.append(i)
    
    
    # Lógica para implementação dos parâmetos para plot único.
    # --------------------------------------------------------
    if (cont_alpha > 1) or (cont_beta > 1) or (cont_mach > 1) :
        print("Mais de um está selecionado por vez.")
        
    
    
    


# =============================================================================
#
# Separa os frames do sistema. A parte da esqueda mostrará o seletor e a parte 
# da direita mostrará os gráficos.
#
# =============================================================================
frame_de_alpha = tkinter.Frame(root)
frame_de_alpha.pack(side = tkinter.LEFT,
                    fill = tkinter.Y)

frame_de_beta  = tkinter.Frame(root)
frame_de_beta.pack(side = tkinter.LEFT,
                   fill = tkinter.Y);

frame_de_mach  = tkinter.Frame(root)
frame_de_mach.pack(side = tkinter.LEFT,
                   fill = tkinter.Y);
                   
frame_plota    = tkinter.Frame(root)
frame_plota.pack(side = tkinter.LEFT,
                 fill = tkinter.Y);                
                
                
# =============================================================================
#
#                                   ALPHA
#
# =============================================================================
alpha_titulo_string = tkinter.StringVar()
alpha               = tkinter.Label(frame_de_alpha,
                                    textvariable   = alpha_titulo_string,
                                    justify        = "left")
alpha_titulo_string.set("ALPHA")
alpha.pack()

# Ângulos -- (-9)
flag_alpha_menos_9 = tkinter.IntVar()
alpha_menos_9      = tkinter.Checkbutton(frame_de_alpha,
                                         text     = "-9",
                                         variable = flag_alpha_menos_9,
                                         onvalue  = 1,
                                         offvalue = 0,
                                         height   = 3,
                                         width    = 10)
alpha_menos_9.pack()

# Ângulos -- (-6)
flag_alpha_menos_6 = tkinter.IntVar()
alpha_menos_6      = tkinter.Checkbutton(frame_de_alpha,
                                         text     = "-6",
                                         variable = flag_alpha_menos_6,
                                         onvalue  = 1,
                                         offvalue = 0,
                                         height   = 3,
                                         width    = 10)
alpha_menos_6.pack()

# Ângulos -- (-3)
flag_alpha_menos_3 = tkinter.IntVar()
alpha_menos_3      = tkinter.Checkbutton(frame_de_alpha,
                                         text     = "-3",
                                         variable = flag_alpha_menos_3,
                                         onvalue  = 1,
                                         offvalue = 0,
                                         height   = 3,
                                         width    = 10)
alpha_menos_3.pack()

# Ângulos -- (0)
flag_alpha_zero = tkinter.IntVar()
alpha_zero      = tkinter.Checkbutton(frame_de_alpha,
                                      text     = "0",
                                      variable = flag_alpha_zero,
                                      onvalue  = 1,
                                      offvalue = 0,
                                      height   = 3,
                                      width    = 10)
alpha_zero.pack()

# Ângulos -- (+3)
flag_alpha_mais_3 = tkinter.IntVar()
alpha_mais_3      = tkinter.Checkbutton(frame_de_alpha,
                                        text     = "+3",
                                        variable = flag_alpha_mais_3,
                                        onvalue  = 1,
                                        offvalue = 0,
                                        height   = 3,
                                        width    = 10)
alpha_mais_3.pack()

# Ângulos -- (+6)
flag_alpha_mais_6 = tkinter.IntVar()
alpha_mais_6      = tkinter.Checkbutton(frame_de_alpha,
                                        text     = "+6",
                                        variable = flag_alpha_mais_6,
                                        onvalue  = 1,
                                        offvalue = 0,
                                        height   = 3,
                                        width    = 10)
alpha_mais_6.pack()

# Ângulos -- (+9)
flag_alpha_mais_9 = tkinter.IntVar()
alpha_mais_9      = tkinter.Checkbutton(frame_de_alpha,
                                        text     = "+9",
                                        variable = flag_alpha_mais_9,
                                        onvalue  = 1,
                                        offvalue = 0,
                                        height   = 3,
                                        width    = 10)
alpha_mais_9.pack()

# =============================================================================
#
#                                   BETA
#
# =============================================================================
beta_titulo_string = tkinter.StringVar()
beta               = tkinter.Label(frame_de_beta,
                                   textvariable   = beta_titulo_string,
                                   justify        = "left")
beta_titulo_string.set("BETA")
beta.pack()

# Ângulos -- (0)
flag_beta_zero = tkinter.IntVar()
beta_zero      = tkinter.Checkbutton(frame_de_beta,
                                     text     = "0",
                                     variable = flag_beta_zero,
                                     onvalue  = 1,
                                     offvalue = 0,
                                     height   = 3,
                                     width    = 10)
beta_zero.pack()

# Ângulos -- (+3)
flag_beta_mais_3 = tkinter.IntVar()
beta_mais_3      = tkinter.Checkbutton(frame_de_beta,
                                       text     = "+3",
                                       variable = flag_beta_mais_3,
                                       onvalue  = 1,
                                       offvalue = 0,
                                       height   = 3,
                                       width    = 10)
beta_mais_3.pack()


# Ângulos -- (+6)
flag_beta_mais_6 = tkinter.IntVar()
beta_mais_6      = tkinter.Checkbutton(frame_de_beta,
                                       text     = "+6",
                                       variable = flag_beta_mais_6,
                                       onvalue  = 1,
                                       offvalue = 0,
                                       height   = 3,
                                       width    = 10)
beta_mais_6.pack()


## =============================================================================
##
##                                   MACH
##
## =============================================================================
mach_titulo_string = tkinter.StringVar()
mach               = tkinter.Label(frame_de_mach,
                                   textvariable   = mach_titulo_string,
                                   justify        = "left")
mach_titulo_string.set("BETA")
mach.pack()

# Velocidade
flag_mach_05 = tkinter.IntVar()
mach_05      = tkinter.Checkbutton(frame_de_mach,
                                   text     = "0",
                                   variable = flag_mach_05,
                                   onvalue  = 1,
                                   offvalue = 0,
                                   height   = 3,
                                   width    = 10)
mach_05.pack()

# =============================================================================
#
#                             Gráfico
#
# =============================================================================
# Gráfico
Grafico = tkinter.Canvas(frame_plota,
                         bg     = "white",
                         height = 600,
                         width  = 800)
Grafico.pack()


fig = matplotlib.figure.Figure(figsize = (8, 6), dpi = 100)
ax1 = fig.add_subplot(111)
ax1.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 9, 2, 7, 1, 10, 11])
ax1.set_xlabel(r'$\alpha$')
figure_canvas_tkagg = FigureCanvasTkAgg(fig, Grafico)
figure_canvas_tkagg.get_tk_widget().pack(fill = tkinter.BOTH)


    


# =============================================================================
#
#                             Botão de Plot
#
# =============================================================================
botao = tkinter.Button(frame_de_alpha, text = "PLOT", command = printa)
botao.pack()

root.mainloop()
