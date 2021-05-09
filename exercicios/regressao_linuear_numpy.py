# Vizualização de dados
import matplotlib.pyplot as plt
import numpy as np

x = [-0.20772428 ,-0.88768748, -0.53481102, -0.11090442, 0.21826496, 0.72771403, 0.91426487]
y = [0.21826496, 0.72771403, 0.91426487,-0.27232914, -0.27598482, -0.51363365, -0.52595711]



#Transformando para numpy e vetor coluna
x, y = np.array(x).reshape(-1 ,1), np.array(y).reshape(-1 , 1)

#Adicionando bias para estimar o termo b
X = np.hstack((x, np.ones(x.shape)))

# Estimando a e b
beta = np.linalg.pinv(X).dot(y)
print('A estimatica ', beta [0][0])
print('B estimativa', beta[1][0])

# plot dos dados
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='Dados Originais')
plt.plot(x , X.dot(beta), label='Regressão Linear')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Regressão LInear")
plt.grid()
plt.show()