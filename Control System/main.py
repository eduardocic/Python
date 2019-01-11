# Importe os parâmetros do sistemas de maneira mais geral para plot e para 
# o tratamento de variáveis complexas.
import matplotlib
import matplotlib.pyplot as plt
import numpy as o
import cmath

# Importe para algo mais específico que faz a simulação do Matlab para trata-
# mento de variáveis similares ao que acontece naquela plataforma.
import control
from control.matlab import TransferFunction
from control.freqplot import bode_plot
from control.freqplot import nyquist_plot


num = 10
den = [1, 10]

sys = TransferFunction(num, den)


w = o.linspace(1, 100, 1000)
bode_plot(sys)
plt.figure()
nyquist_plot(sys)
plt.grid()