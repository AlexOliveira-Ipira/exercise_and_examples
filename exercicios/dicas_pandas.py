import pandas as pd


# Lendo arquivo csv com pandas, buscando os dados direto no servidor
df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")


# Group by
group_by = df.groupby(by='classification')
# Gerado o objeto
print(group_by)

# Aplicar função no agrupamento

# Funçào desse exemplo Media
group_by_media = df.groupby(by='classification').mean()
print(group_by_media)

# Função desse exemplo soma
group_by_soma = df.groupby(by='classification').sum()
print(group_by_soma)

# Remover uma coluna - Ideal sempre criar uma copia do df e então execultar o drop
df2 = df.copy() # Essa é a forma correta de fazer a copia
#df2 = df # Essa faz a duplicação da df e se for feito qualquer alteraçào no df2 sera feita no df
novo_df = df2.drop('temperatura', axis=1)
print(novo_df)

