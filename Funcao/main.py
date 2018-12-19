""" Estou colocando esses valores como padrão pois eu desejo utilizar 
    os gráficos e também fazer manipulações algébricas """
import matplotlib
import matplotlib.pyplot as plt
import numpy as o

""" Importando os parâmetros de funções definidas em outro arquivo """
from funcoes import fatorial
from funcoes import dobro

""" Cálculo do fatorial """
for i in range(0, 10, 1):
    print("O fatorial de ", i, " é: ", fatorial(i))
print()

""" Cálculo do dobro """
for i in range(0, 10, 1):
    print("O dobro de ", i, " é: ", dobro(i))

