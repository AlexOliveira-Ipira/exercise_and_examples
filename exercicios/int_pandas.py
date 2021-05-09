import pandas as pd


# Lendo arquivo csv com pandas, buscando os dados direto no servidor
df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")

"""
Exemplo de como carregar arquvios em excel

Criando a base de dados
excel_file = pd.ExcelFile('Caminho do arquiov')

df = pd.read_excel(excel_file, sheet_name='nome da aba da planilha')
"""

#Visualizar as primeiras 'N' linhas
n = 3
print(df.head(n))

# Visualizar as ultimas 'N' linhas
n = 3
print(df.tail(n))

# Verificar tipos de dados
print(df.dtypes)

# Estatistica basica
print(df.describe())

# Dataframe info
print(df.info())

# Nome das colunas
print(df.columns)
