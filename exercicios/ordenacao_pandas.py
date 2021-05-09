import pandas as pd

# Lendo arquivo csv com pandas, buscando os dados direto no servidor
df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")

# Ordenação crescente por uma coluna
order_temp = df.sort_values(by='temperatura')
print(f'Ordenando apenas com uma coluna: \n', order_temp)

# Ordenaçào crescente com duas colunas - Ordena sempre no primeiro elemento e depois sucessivamente
order_tem_clas = df.sort_values(by = ['classification' , 'temperatura'])
print(order_tem_clas)
print()

# Ordenaçào decrescente de uma coluna
order_dec_clas = df.sort_values(by='classification', ascending=False)
print(order_dec_clas)
print()

# Order crescente pelo index
order_index = df.sort_index()
print('Order crescente pelo index: ',order_index)
print()

# Order decrescente pelo index
order_index_decres = df.sort_index(ascending=False)
print('Order decrescente pelo index: ', order_index_decres)
print()
