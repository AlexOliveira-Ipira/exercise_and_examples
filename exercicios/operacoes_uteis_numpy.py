import numpy as np

#Criando base de dados para trabalhar
x = np.array([[1, 3, 7],
             [4, 11, 21],
             [42, 8, 9]])
print('X : \n', x)
print()

# Metodo reshap - Transforma a matiz em um vetor coluna
print('Transformação em um vetor coluna: \n', x.reshape(9, 1))
print()

# Exemplo de transposição de matriz
print('X transposição: \n', x.T)
print()

# Exemplo de np.sum - Soma em um dado eixo, axis ( 0: linha, 1: Coluna)
print('X:\n', x)
print('Soma de todos elementos de X: \n', np.sum(x))
print('Soma de X ao longo das linha: \n', np.sum(x, axis=0))
print('Soma de X ao longo das coluna: \n', np.sum(x, axis=1))
print()

# Exemplo de np.mean - Media em um dado eixo - axis (0: linha, 1: Coluna)
print('X:\n', x)
print('Media de todos elementos de X: \n', np.mean(x))
print('Media de X ao longo das linha: \n', np.mean(x, axis=0))
print('Media de X ao longo das coluna: \n', np.mean(x, axis=1))
print()

# Exemplo do np.median - É a mesma sintax do np.mean so que retorna a mediana
print('X:\n', x)
print('Mediana de todos elementos de X: \n', np.median(x))
print('Mediana de X ao longo das linha: \n', np.median(x, axis=0))
print('Mediana de X ao longo das coluna: \n', np.median(x, axis=1))
print()

# Exemplo de np.where - Retona nos indices onde uma dada condição é atendida
cond_pares = x % 2 == 0 # Numeros pares
print('Condição : \n', cond_pares)
i , j = np.where(cond_pares)
print('Indicide i , linha:', i)
print('Indice j , coluna: ', j)

# Selecionando as linhas de X que contem algum numero par
print('X:\n', x)
cond_pares = x % 2 == 0 # Numeros pares
print('Condição : \n', cond_pares)

# Se ouver algum numero par retornar
i_row = np.where(np.sum(cond_pares, axis=1))[0]
print('Indice das linhas que possuem os numers pares:', i_row)
print('Linhas que possuem os numeros pares:\n ', x[i_row, :])


