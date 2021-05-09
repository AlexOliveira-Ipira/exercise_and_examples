import numpy as np

#Abre o help  da biblioteca
#help(np.array)

#Criando um array 1D: [1,2,3]
print('Exemplos de array de 1 dimensão')
l = [1,2,3]
x = np.array(l)
print('X:', x) #Elementos contidos no array
#Quantidade de elemesntos no array , nesse exemplo temos apenas 1 elemento.
print('Shap:', x.shape)
print()

#Criando aray 2D: Listas aninhada
print('Exemplos de array de 2 dimensão')
l = [[1,2],[3,4]]
x = np.array(l)
print('X:\n', x)
# Quantidade de elemesntos no array , nesse exemplo temos 2 elementos nas linhas
# e 2 elemesntos nas colunas
print('Shap:', x.shape)
print()

#Funções para criação de arrays

#np.zeros - Criar array composto de zeros
print('Exemplo de arrey criado com a função np.zeros')
dim = (2,2) #Linhas , Colunas
x = np.zeros(dim)
print("X: \n", x)
print('Shap:', x.shape)
print()

#np.ones - Criar array composto de um
print('Exemplo de arrey criado com a função np.ones')
size = (2, 2) #Linhas , Colunas
x = np.ones (size)
print("X: \n", x)
print('Shap:', x.shape)
print()


#Criando Valores dentro de um intervalo
#valores uniformes entre 5 , 15 com quantdade de 6
print('Exemplo de cração de Array com inicio , fim e quantidade maxima')
print('Iniciando com 5 , finalizando em 15 com quantidade de 6')
x_min , x_max, num_max = 5, 15, 6
x = np.linspace(start=x_min, stop= x_max, num=num_max)
print("X:", x)
print('Shap:', x.shape)
print()

#Criando a matriz de indentidade
print('Exempl de criação de array de matriz diagonal, ficando o 1 no cetro ')
print('e em torno dele os zeros')
n = 4
x = np.eye(n)
print('X:\n', x)
print('Shap:', x.shape)
print()

#Criando array de valores aleatoreos utilizando o np.random.random
print('Exemplo de criação de array de numeros aleatores, entre 0,0 e 1,0')
print('utilizando o metodo np.random.random.')
x = np.random.random(size=(2,3))
print('X:\n', x)
print('Shap:', x.shape)
print()