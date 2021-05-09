import numpy as np

#Criando base de dados para os exmplos
x = np.array([[1,2], [3, 4]])
y = np.array([1.5, 3.5])
print("X : \n", x)
print('Y : \n', y)
print()


#Exemplo de comarações entre array
print(x)
print('Comparação de um array com uma (>): \n ', x > 2)
print('Comparação de um array com uma (>=): \n', x >= 2)
print('Comparação de um array com uma (<): \n', x < 2)
print('Comparação de um array com uma (<=):\n', x <= 2)
print('Comparação entre array utilizando (==): \n ', x == y)
print('Comparação entre array utilizando (>): \n', x > x)
print('Comparação entre array utilizando (>): \n', x < y)

# Exemplo de idexaçào boleana novos array
x = np.array([[1, 3, 7],
             [4, 11, 21],
             [42, 8, 9]])
print('X : \n', x)
print()

# Exemplo de uso da indexação boleana, retrnar os valores maiso que o valor de K
k = 10
cond = x > k
print('Condição: \n', cond)
print(f'Elemento maiora que {k}:', x[cond])
print(f'Numero de elementos mairo que {k}:', len(x[cond]))

# Exemplo de uso de conição boleana, extraindo somente os valores pares
cond_pares = x % 2 == 0 # Numeros pares
print('Condição : \n', cond_pares)
print('Numeros pares: \n', x[cond_pares])

# Exemplo de uso de conição boleana, extraindo somente os valores impares
cond_imp = x % 2 != 0 # Numeros pares
print('Condição : \n', cond_imp)
print('Numeros pares: \n', x[cond_imp])


