from itertools import combinations
import pandas as pd

lst_posicoes = []
vlrs_pos = []
dados = {}
linha_dados = {}
pos = int(input('\n>>>>> DEFINA O NÚMEROS DE POSIÇÕES PARA SEU JOGO: '))
for i in range(0, pos):
    lst_posicoes.append(f'P{i}')

tipo_jogo = int(input('\nDigite o tipo de jogo:\n\
                      ( 2 ) - Para Dupla\n\
                      ( 3 ) - Para Trio\n\
                      ( 4 ) - Para Quadra\n\
                      >>>>> Resposta: '))

for pos in lst_posicoes:
    for i in range(0, tipo_jogo):
        vlr_pos = int(input(f'n>>>>> DEFINA O {i+1}º VALOR (de 1 à 100) PARA POSIÇÃO {pos}: '))
        vlrs_pos.append(vlr_pos)
    dados[pos] = vlrs_pos
    vlrs_pos = []

n_jogo_linha = int(input('\n>>>>> DEFINA A QUANTIDADE DE JOGOS POR LINHA PARA RESULTADO: '))
posicoes = combinations(lst_posicoes, n_jogo_linha)
linha = 0
for p in posicoes:
    linha += 1
    res = []
    for value in p:
        res.extend(dados[value])
    linha_dados[linha] = res


df = df = pd.DataFrame.from_dict(data=linha_dados, orient='index')
df.to_excel('C:\\Users\\gogon\\Downloads\\resultados_JORGE.xlsx')
