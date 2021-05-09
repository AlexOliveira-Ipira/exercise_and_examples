import numpy as np

# Criando dos array 2d para utilizar nos exemplos
x = np.ones([2,2])
y = np.eye(2)
print('X:\n', x)
print('Y:\n ', y)
print()


# Multiplicação
print('Miltiplicação entre dois array: \n', x * y)
print('Multiplicação float / int: \n', x * 2)
print()

# Multiplicação matricial
print('Multiplicado matrical (np.dot): \n', np.dot(x,y))
print('Multiplicado matrical (@): \n', x @ y)
print('Multiplicado matrical (.dot): \n', x.dot(y))
print()

"""
Exemplo de utilziaçào de multiplicação de array para resolver uma equação

Soluções de um sistema de equções
    a + 2*b = 7
    3*a - 2*4 = -11
    Solução analitica: (a,b) = (-1,4)
Matricialmente , este probelma tem a seguint forma:
Ax = x onde:
 x = [a,b]
 A = [[1, 2] , [3, -2]]
 c = [7 , -11]
 Solução numerica: x = inv(A) @ c,
"""

# Definição do problema
A = np.array([[1, 2], [3, -2]])
C = np.array([[7], [-11]])
print('A : \n', A)
print('C : \n', C)

# Solução
x = np.dot(np.linalg.inv(A), C)
#x = np.linalg.inv(A) @ C
print('a , b:', x.ravel())




