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

# Plot simples para apresentaçào dos dados numericos, no nosso exemplo a Data e a Temperatura
df.plot()

# Definindo um tamanho para o plote
df.plot(figsize=(10,5))

# Definindo linhas para o plot
df.plot(figsize=(10,5), grid=True)

# Plotando linhas stailes
df.plot(style='-o', figsize = (10,5), grid=True)
df.plot(style='-', figsize = (10,5), grid=True)
df.plot(style='.', figsize = (10,5), grid=True)

# Plotando usando a função linewidth - Aumenta a largura das linha
df.plot(style='-o', linewidth = 2.5, figsize=(10,5), grid=True)

# Definindo cor da linha - color
df.plot(style='-o', linewidth = 2.5, color ='red' , figsize=(10,5), grid=True)

# Utilizando o metodo value_counts para contar quantidade de dados repetidos
cont_qtd = df['classification'].value_counts()
print(cont_qtd)

# Plot Barras - rot = rotação do label no grafico
df['classification'].value_counts().plot.bar(figsize=(10,5), rot=0)


# pie plot - Plot pizza
df['classification'].value_counts().plot.pie( autopct='%1.1f%', shadow=True, figsize=(10,5), rot=0)

