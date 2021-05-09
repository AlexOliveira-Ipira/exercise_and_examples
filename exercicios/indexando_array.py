import numpy as np

#Criando base de dados para os exmplos
x = np.linspace(start=10, stop=100, num=10)
print('X: \n', x)
print('Sharp : ', x.shape)
print()

#Extração de elementos
print('X:\n', x)
print('Primeiro elemento:', x[0])
print('Segundo elemento:', x[1])
print('Acessando o ultimo elemento, usando a posição do indice :', x[9])
print('Acessando o ultimo elemento, usando o inidice negativo -1', x[-1])
print()

#Exemplo do uso do slice para acessar os elementos
print('X: \n', x)
print('Os dois primeiros elementos:', x[0:2])
print('Os dois primeiro elemensoto sem colocar o primeiro inteiro', x[:2])
print('Os dois ultimos elementos:',x[-2:])
print()

#Exemplo de slice com array 20 matrizes
x = x.reshape(2,5) #Criar um array 2D com 5 colunas
print('X; \n', x)
print()

#Extraidno elementos de array 2D
print('X; \n', x)
print('Primeira Linha, segunda coluna', x[0, 1])
print('Segunda Linha, penultima coluna', x[1, -2])
print('Ultima Linha, ultima coluna', x[1, 4])
print('Ultima Linha, ultima coluna', x[-1, -1])
print()

#Exemplo de slice acessando todos os elementos do array 2D
print('X \n ', x)
print('Primeira linha inteira',x [0, :])
print('Primeira linha, segunda a quarta coluna', x[0, 1:4])
print('Ultima cluna inteira: \n', x[:, [-1]]) #Usando os [] imprime em linhas diferentes
print('Ultima cluna inteira: \n', x[:, -1]) #Não usando os [] imprime em linhas iguais
print()

#Dois metodos para alterar ou copiar os dados do array
#Nes metodo o valor é substituido
print('Não utilizando o metodo copy, dessa forma o valor de X é alterado')
x = np.array([1,2,3])
print("Valor de X antes:", x)
y = x[:2]
y[0]= -100 # Trocando o valor do primeiro indice
print('Valor de X depois:', x)
print()

#Preservando os dados de X
print('Usando o metodo copy para preservar o valor de X')
x = np.array([1,2,3])
print('Valor de X antes:', x)
y = x[:2].copy()
y[0] = -100
print('Valor de X depois', x)
print()
