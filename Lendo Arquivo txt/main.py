#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 11:45:42 2018

@author: eduardo
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

arquivo = open("saida.txt", "r")


""" 
Para utilização da função 'help', você faz o seguinte 'help(arquivo)'.
    
No caso, eu não sei quais são os métodos do objeto 'arquivo'. Com isso eu 
saberei quais são tais métodos.
"""

#help(arquivo)

""" Para ler todo o arquivo """
Linhas = arquivo.readlines()

""" Para o cálculo inicial do sistema """
intermed = Linhas.__getitem__(0)
intermed = intermed.split()

""" Criação de estruturas para composição de valores """
t     = []
valor = []

""" Inserindo os primeiros elementos """
t.append(float(intermed[0]))
valor.append(float(intermed[1]))

""" Fazendo o 'for' para a criação dos vetores que serão plotados """
for i in range(0, 230, 1):
    intermed = Linhas.__getitem__(i)
    intermed = intermed.split()
    temp = float(intermed[0])
    t.append(temp)
    temp = float(intermed[1])
    valor.append(temp)


""" Plotando os valores """
plt.plot(t, valor, '--b')
plt.xlabel("tempo (s)")
plt.ylabel("Cosseno")
plt.grid()
plt.title("Gráfico doido da peste")




