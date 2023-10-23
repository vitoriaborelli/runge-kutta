import sys
import matplotlib.pyplot as plt
from math import *

# Definindo a função a qual que será aplicado o método

possible_operators = {'sqrt': sqrt, 'e': e, 'exp': exp, 'pi': pi, 'sin': sin, 'cos': cos, 'tan': tan, 'log': log, 'log10': log10}

print("Insira a função que será utilizada: ")
f = str(input("y'(x) = "))

def funcao(x,y):
    funcao = eval(f, possible_operators, {'x': x, 'y': y})
    return funcao 

# Leitura do x inicial

print("\nInsira o valor inicial de x:")
x = []
inicial = []
x.append(float(input('x_inicial = ')))
inicial.append(float(input('x_inicial_lagrange = ')))
# Leitura do y inicial 

print("\nInsira o valor inicial de y: ")
y = []
y.append(float(input('y_inicial = ')))

# Leitura do h (incremento)

print("\nInsira o valor do incremento (passo):")
h = float(input('h = '))

# Leitura do número de iterações

print('\nComo gostaria de definir o número de iterações?')
print('\n0: Quantidade de Pontos')
print('1: Valor Máximo de x\n')

tipo = int(input())

if (tipo == 0):
  print("\nInsira o número de pontos da tabela:")
  n = int(input('n = '))

elif (tipo == 1):
  print("\nInsira o valor máximo de x usado para o cálculo:")
  xmax = float(input('x_max = '))
  n = ((xmax - x[0])/h)+1

  if (int(n) == round(n, 10)):
    n = int(n)
  else:
    sys.exit("\nIntervalo Inválido")

else:
  sys.exit("\nValor inserido não corresponde a nenhuma das opções dadas")

# Definindo o método

def rungeKutta4Ordem (x, y, h):

        R1 = h * funcao(x, y)
        R2 = h * funcao(x + 0.5 * h, y + 0.5 * R1)
        R3 = h * funcao(x + 0.5 * h, y + 0.5 * R2)
        R4 = h * funcao(x + h, y + R3)
        y = y + (R1+2*R2+2*R3+R4) / 6

        return y



# Aplicando a função e imprimindo os resultados 

print("\n  x          y")
print("--------------------")

for i in range(n):

      print('%.2f\t%.10f' % (x[i], y[i]))
      y.append(rungeKutta4Ordem(x[i],y[i],h))
      x.append(x[i] + h)

# Exibição do gráfico resultante da a partir da tabela obtida 

print("\n")
plt.plot(x, y)
plt.title('Função Resultante')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# Lagrange Interpolation

# Importing NumPy Library
import numpy as npy

# Making numpy array of n & n x n size and initializing 
# to zero for storing x and y value along with differences of y
x = npy.zeros((n))
y = npy.zeros((n))

# Set interpolated value initially to zero
yp = 0

# Implementing Lagrange Interpolation
for i in range(n):
    
    p = 1
    
    for j in range(n):
        if i != j:
            p = p * ((inicial[0] + h*n ) - x[j])/(x[i] - x[j])
    
    yp = yp + p * y[i]    

# Displaying output
print('%.2f\t%.10f' % (inicial[n]))
print("p("+str(x)+")=",pny)
