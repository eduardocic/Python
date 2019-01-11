import matplotlib
import matplotlib.pyplot as plt
import numpy as o
import cmath

# Número 'pi'.
pi  = cmath.pi

# Vetor discreto e frequência.
x = [1, 1, 1, 1, 1]
T = 0.01
f = 100
w = o.linspace(0, 2*pi*f, 1000)


# Definição dos termos de soma
SOMA = []
for i in range(0, 1000):
    soma = 0
    for k in range(0, o.size(x)):
        # Número complexo.
        num  = complex(0, -k*w[i]*T)    
        # Exponencial do número.
        EXP  = cmath.exp(num)  
        soma = soma + EXP*x[k]
    SOMA.append(soma)
    
    
# Ajuste de fase e de módulo.
fase   = []
modulo = []
for i in range(0, 1000):    
    fase.append(cmath.phase(SOMA[i]))
    modulo.append(abs(SOMA[i]))
    

# Plota o resultado dentro de uma perspectiva de rad/s.
# Caso se deseje fazer uma análise de parâmetros normalizados, a gente divide 
# pelo parâmetro.    
plt.subplot(2,1,1)    
plt.plot(w, modulo)
plt.xlabel("Frequência (rad/s)")
plt.ylabel("Módulo")
plt.grid()
plt.title("Transformada de Fourier Discreta na Força Bruta")

plt.subplot(2,1,2)
plt.plot(w, fase)
plt.xlabel("Frequência (rad/s)")
plt.ylabel("Fase")
plt.grid()

    
    
    
    
     

