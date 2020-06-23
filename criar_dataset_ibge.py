import pandas as pd
import numpy as np

# coletar dados de pib
df_pib = pd.read_excel("dados_publicos/PIB dos Municipios - base de dados 2010-2017.xls")


# filtrar ano mais recente
df_pib = df_pib[df_pib['Ano'] == np.max(df_pib['Ano'])]
# selecionar colunas
df_pib = df_pib[['Código do Município',
                 'Nome do Município',
                 'Sigla da Unidade da Federação',
                'Produto Interno Bruto per capita, \na preços correntes\n(R$ 1,00)']]
# renomear colunas
df_pib.columns = ['codigo_municipio', 'nome_municipio', 'sigla_uf', 'pib_per_capita']

# coletar dados de população e idhm
df_idhm = pd.read_excel('dados_publicos/atlas2013_dadosbrutos_pt.xlsx', sheet_name = 'MUN 91-00-10')


# filtrar ano mais recente
df_idhm = df_idhm[df_idhm['ANO'] == np.max(df_idhm['ANO'])]
# selecionar colunas
df_idhm = df_idhm[['Codmun7', 'pesotot', 'IDHM']]
# renomear colunas
df_idhm.columns = ['codigo_municipio', 'populacao_total', 'idhm']
df_idhm.head()

# juntar os datasets publicos
df_ibge = df_pib.merge(df_idhm, on = 'codigo_municipio', how = 'left')
# exportar csv
df_ibge.to_csv('dados_municipios_ibge.csv', index = False)
print('Dataset criado')