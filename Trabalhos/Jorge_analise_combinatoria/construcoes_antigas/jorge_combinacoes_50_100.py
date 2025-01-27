from itertools import combinations
import pandas as pd
from dotenv import load_dotenv
from os import getenv


load_dotenv()
# Dict para armazenar por linha os resultados da combinacao
res = {}
# Numero de combinacoes por linha
comb = 5
# Qtd de numeros para o jogo
lim = 100
# Lista de numero para combinacao
lst_num = []
# Nomes para coluna do DF
coluns = []
# Numeros por linha do jogo para ser combinado
linJ = {}

# Qtd de colunas no jogo
col = 5
# Criacao de lista que formara coluna dos resultados
for c in range(1, col+1):
    coluns.append('Col_' + str(c))
coluns.append('LinJ')

# Criacao da lista
cont = 1
linha = 0
for i in range(1, lim+2):
    if cont < 11:
        cont += 1
        lst_num.append(i)
    elif cont > 10:
        linha += 1
        cont = 2
        linJ[linha] = lst_num
        lst_num = []
        lst_num.append(i)
# print(linJ)
# Padrao de onde sera salvo arquivo
table = getenv("loc_name_xls")
linha = 0

# Biblioteca para analise combinatoria
for linha_jogo, nums in linJ.items():
    combinacoes = list(combinations(nums, comb))
    # Criacao do dict com lin no (key) e resultado no (value)
    for i in combinacoes:
        linha += 1
        num_in_lin = []
        for val in i:
            num_in_lin.append(val)
        num_in_lin.append(linha_jogo)
        res[linha] = num_in_lin

# Montagem do DF
df = pd.DataFrame.from_dict(data=res, orient='index', columns=coluns)
print(df)
indice_filtrado = []
# Separacao dos indices que tem 5 resultados impar
impar_indice_M5 = []
# Separacao dos indices que tem 5 resultados par
par_indice_M5 = []

# Laco em cada linha do DF para validar se temos 5 resultados par ou impar
for indice, linha in df.iterrows():
    count_impar = 0
    count_par = 0
    for v in linha:
        if v % 2 == 0:
            count_par += 1
        else:
            count_impar += 1
    if count_impar == 5:
        impar_indice_M5.append(indice)
    elif count_par == 5:
        par_indice_M5.append(indice)

# Ordenacao das duas listas de indice com par e impar para remover
# tais resultados
impar_par = impar_indice_M5 + par_indice_M5
# Ordenacao dos indices
ord_impar_par = sorted(impar_par)

# DF sem impar e par com 5 resultados em uma linha
df_1 = df[~df.index.isin(ord_impar_par)]

'''
df1 = df_1.loc[(df_1['Col_1'] < 11) & (df_1['Col_2'] < 11)
               & (df_1['Col_3'] < 11) & (df_1['Col_4'] < 11)
               & (df_1['Col_5'] < 11)]

df2 = df_1.loc[(df_1['Col_1'].between(11, 20)) & (df_1['Col_2'].between(11, 20))
               & (df_1['Col_3'].between(11, 20)) & (df_1['Col_4'].between(11, 20))
               & (df_1['Col_5'].between(11, 20))]
'''


df_1.to_excel(table)
print('finalizado')
