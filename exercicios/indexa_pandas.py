import pandas as pd

# Lendo arquivo csv com pandas, buscando os dados direto no servidor
df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")

# Exemplo de converção de uaa coluna no pandas, nesse exemplo
#será convertido a coluna date que veio como object
print('Antes de converção :', df.dtypes['date'])
df['date'] = pd.to_datetime(df['date'])
print()
print('Depois da converção :', df.dtypes['date'])

# Setando o idice, no exemplo esta sendo usado a coluna data
df = df.set_index('date')
print(df)
print()


#Indexação boleana considerando a temperatura
temp_atual1 = df['temperatura'] >=25 # Indexação que mostra apenas se True ou False
temp_atual2 = df[df['temperatura']>=25] # Indexação que mostra a temperatura

print(f'A indexação que mostra apenas True ou Fals {temp_atual1}')
print()
print(f'A indexação que mostra a temperatura:\n{temp_atual2}')
print()

#Indexação boleana considerando datatime
data_nova= df[df.index <='2020-03-01']
print(data_nova)
print()

# Exemplo selecionando uma data expecifica e uma coluna
# com loc
print('Metodo loc')
nova_coluna_loc = df.loc[df.index<='2020-03-01', ['classification']]
print(f'Temperatura nos dias abaixo de 01/03/2020:\n {nova_coluna_loc}')
print()

# Exemplo selecionando uma data expecifica e uma coluna
# com o iloc
print('Metodo iloc')
nova_coluna_iloc = df.iloc[df.index<= '2020-03-01', [-1]]
print(f'Temperatura nos datas abaico de 01/03/2020: \n {nova_coluna_iloc}')
