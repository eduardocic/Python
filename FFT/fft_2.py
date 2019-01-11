import matplotlib
import matplotlib.pyplot as plt
import numpy as o
import cmath

# Número 'pi'.
pi  = cmath.pi

# Tempo total do sinal.
t = o.linspace(0, 1.5, 1500)
x = []
for i in range(0, o.size(t)):
    x.append((0.7)*cmath.sin(2*pi*50*t[i]) + cmath.sin(2*pi*120*t[i]))
    
T = 0.001
f = 1/T
MAX = 10000
w = o.linspace(0, 2*pi*f, MAX)

# Definição dos termos de soma
SOMA = []
for i in range(0, MAX):
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
for i in range(0, MAX):    
    fase.append(cmath.phase(SOMA[i]))
    modulo.append(abs(SOMA[i]))

# Olhando na ótica de frequências do sistema, é interessante entender que
# para as frequências em Hz, o que a gente olha é o espectro até metade da 
# frequência de amostragem. Sendo assim, perceba que:

plt.figure()
plt.subplot(2,1,1)    
plt.plot(w/(2*pi), modulo)
plt.xlabel("Frequência (rad/s)")
plt.ylabel("Módulo")
plt.grid()

plt.subplot(2,1,2)
plt.plot(w/(2*pi), fase)
plt.xlabel("Frequência (rad/s)")
plt.ylabel("Fase")
plt.grid()
