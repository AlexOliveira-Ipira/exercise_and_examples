import numpy as np

# Criando dos array 2d para utilizar nos exemplos
x = np.ones([2,2])
y = np.eye(2)
print('X:\n', x)
print('Y:\n ', y)

# soma
print('Soma de dois array\n', x + y)
print()
print('Soma de float / int :\n', x + 2) #broadcasting
print()

# Subtração
print('Soma de dois array\n', x - y)
print()
print('Soma de float / int :\n', x - 2) #broadcasting
print()

"""
# Divisão
print('Soma de dois array\n', x / y) # Neste processo vai dar um erro devido a divisão por zero
print()
print('Soma de float / int :\n', x / 2) #broadcasting
print()

Quando o brodcasting não funciona, retira o comentário dessa linha para ver a descrçào
do erro:
print('Erro no processo do brodcas, devido ao numero de array diferente entre eles')
print(np.array([1, 2, 3]) + np.array([1, 2]))
print()
"""

# Soma, Subração de Divisão
print('Combinando operações: \n', (x+y)/(x-2))
