from classes.tipo_jogo import Jogo
from classes.combinacoes import AnaliseCombinatoria

lst_campos = []
linha_dados = {}

pos = int(input('\n\t>>>>>\tDEFINA A QUANTIDADE DE CAMPOS PARA SEU JOGO: '))
for i in range(0, pos):
    lst_campos.append(f'P{i}')

tipo_jogo = int(input('\t\tDigite o tipo de jogo:\n\
                      ( 2 ) - Para Dupla\n\
                      ( 3 ) - Para Trio\n\
                      ( 4 ) - Para Quadra\n\
                      \t\t\t>>>>> Resposta: '))

input_dados = Jogo(lst_campos, tipo_jogo)
dados_arranjados, tipo_jogo = input_dados.definir_vlrs_campos()
n_jogos_por_res = int(input(f'\n>>>>> DEFINA QTD DE {tipo_jogo} '
                            f'POR RESULTADO: '))
infos_analisar = AnaliseCombinatoria(lst_campos, n_jogos_por_res,
                                     dados_arranjados)
combinacoes = infos_analisar.combinar_campos()
