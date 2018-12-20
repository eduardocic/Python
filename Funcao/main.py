###############################################################################
#
# Estou colocando esses valores como padrão pois eu desejo utilizar os gráficos
# e também fazer manipulações algébricas.
#
###############################################################################
import matplotlib
import matplotlib.pyplot as plt
import numpy as o

# Importando os parâmetros de funções definidas em outro arquivo.
from funcoes import fatorial
from funcoes import dobro

# Cálculo do fatorial.
for i in range(0, 10, 1):
    print("O fatorial de ", i, " é: ", fatorial(i))
print()

# Cálculo do dobro.
for i in range(0, 10, 1):
    print("O dobro de ", i, " é: ", dobro(i))

alpha = o.linspace(0, 10, 100)
beta  = alpha*2

# This function returns a tuple 
def fun(): 
    str = "geeksforgeeks"
    x   = fatorial(8)
    return [str, x];  # Return tuple, we could also 
                    # write (str, x) 
  
# Driver code to test above method 
[str, x] = fun() # Assign returned tuple 
print(str) 
print(x) 