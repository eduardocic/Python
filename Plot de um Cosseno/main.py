import matplotlib
import matplotlib.pyplot as plt
import numpy as o


x, COS, SEN = [], [], []


for i in range(0, 360, 1):
    x.append(i)
    COS.append(o.cos((o.pi)*i/180))
    SEN.append(o.sin((o.pi)*i/180))


""" Plot do resultado do sistema """
plt.plot(x, COS, label = 'cosseno') 
plt.hold
plt.plot(x, SEN, '-r', label = 'seno')
plt.xlabel("Graus")
plt.ylabel("Resultado")
plt.title("Seno e Cosseno")
plt.grid()
plt.legend()

""" Plotando em outra figura """
plt.figure()
plt.plot(x, COS, label = 'cosseno') 
plt.xlabel("Graus")
plt.ylabel("Resultado")
plt.grid()



