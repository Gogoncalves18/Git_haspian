import pandas as pd
import numpy as np
import tratamento_dados as treat

# Define numero de colunas ilimitadas para mostra na tela
pd.set_option('display.max_columns', None)
df = pd.read_csv("C:\git\Git_haspian\Trabalhos\Implanew\DADOS IMPLANEW.csv",
                 sep=';')
# Elimina os trechos sem valor no DF com a coluna codigo
df = df[df['CODIGO'].notnull()]
# Coloca '-' em todo campo vazio
df = df.fillna('-')
# print(df[df.isnull().any(axis=1)])

for linha in range(len(df)):
    # Leio as 18 colunas no df
    for i in range(1, 18):
        # Localica a celula em questao e aciona a funcao para converter
        # os caracteres e padronizar eles, o cliente escrevia a
        # mesma informação de modos diferentes
        dado = df[f'DIM_{i}'].iloc[linha]
        df[f'DIM_{i}'].iloc[linha] = treat.conversao_dado(dado)
        dado = df[f'SUP_{i}'].iloc[linha]
        df[f'SUP_{i}'].iloc[linha] = treat.conversao_dado(dado)
        dado = df[f'INF_{i}'].iloc[linha]
        df[f'INF_{i}'].iloc[linha] = treat.conversao_dado(dado)

print('\n>>> PASSOU PELA CONVERSAO')

# Lista para separar a sequencia de dados em um novo DF
PartCode = []
Description = []
NominalValue = []
MinValue = []
MaxValue = []

for ind, linha in df.iterrows():
    # Roda o DF novamente interando em linha a linha de cada
    # Coluna para salvar nas listas
    for i in range(1, 18):
        PartCode.append(linha['CODIGO'])
        Description.append(f'{linha[f'ITEM_{i}']} {linha[f'CRITERIO_{i}']}')
        NominalValue.append(f'{linha[f'DIM_{i}']}')
        MaxValue.append(f'{linha[f'SUP_{i}']}')
        MinValue.append(f'{linha[f'INF_{i}']}')

print('\n>>> PASSOU PELA APPEND DE DADOS')

# Montagem do novo DF
df_implanew = pd.DataFrame(data={'PartCode': PartCode,
                                 'Description': Description,
                                 'NominalValue': NominalValue,
                                 'MaxValue': MaxValue,
                                 'MinValue': MinValue
                                 }
                           )

print('\n>>> MONTOU O DF_IMPLANEW')


for linha in range(len(df_implanew)):
    # Gera uma nova coluna convertendo o dado em numero, se ele
    # gerar erro, é adicionado o valor ATTR, assim sabesse qual é
    # texto e não numero
    df_implanew['Tipo'] = pd.to_numeric(df_implanew['NominalValue'],
                                        errors='coerce').replace(np.nan,
                                                                 'ATTR')

# Gera um DF so de textos
df_implanew_txt = df_implanew[df_implanew['Tipo'] == 'ATTR']
print('\n>>> CRIOU DF DE ATTR')

# Gera um DF so de dimensoes
df_implanew_num = df_implanew[df_implanew['Tipo'] != 'ATTR']
print('\n>>> CRIOU DF DE NUMS')

# Converte a coluna em float
df_implanew_num['NominalValue'] = df_implanew_num['NominalValue'].astype(
                                                                 'float')
df_implanew_num['MaxValue'] = df_implanew_num['MaxValue'].astype('float')
df_implanew_num['MinValue'] = df_implanew_num['MinValue'].astype('float')
# Remove a coluna final
df_implanew_num = df_implanew_num.drop(columns=['Tipo'], axis=1)

# Transforma o valor de máxima e minimo em valores nominais
df_implanew_num['MaxValue'] = df_implanew_num['NominalValue'] +\
                              df_implanew_num['MaxValue']
df_implanew_num['MinValue'] = df_implanew_num['NominalValue'] +\
                              df_implanew_num['MinValue']

print('\n>>> LIMPOU A CONVERSAO E COLUNA DO DF NUMS')

df_implanew_txt = df_implanew_txt.drop(columns=['Tipo'], axis=1)
print('\n>>> LIMPOU A CONVERSAO E COLUNA DO DF txt')

# Salva a tabela
df_implanew_num.to_excel('C:\\git\\Git_haspian\\Trabalhos\\Implanew\\implanew_dims.xlsx', index=False)
df_implanew_txt.to_excel('C:\\git\\Git_haspian\\Trabalhos\\Implanew\\implanew_attr.xlsx', index=False)
