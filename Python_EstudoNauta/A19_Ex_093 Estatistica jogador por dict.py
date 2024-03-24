'''Criar um programa que gerencie a estatica de um jogador.
Gerenciar o numero de jogos e gols por jogos e total de gols.
Guardar tudo em um dicionario e posterior apresentar:
-Valor de cada campo
-Numero de partidas
-Gols em cada partida
-Total de gols
'''
estat_player = {}  # Guarda todos os dados
lst_gols = []  # Lista somente para gerar copia para dentro do Dict
gols_ = 0  # variavel para somar gols
estat_player['nome'] = str(input('\nNome do Jogador: '))
estat_player['num_jogos'] = int(input('\nQdts jogos foram registrados: '))
for n in range(0, estat_player['num_jogos']):  # Loop sobre o num de
    # jogos dentro do dict
    lst_gols.append(int(input('\nQuantos gols ele fez na partida : ')))
estat_player['gols'] = lst_gols.copy()
# Inseri os gols como lista no campo V de uma K
for g in estat_player['gols']:  # contagem de gols
    gols_ += g
estat_player['tot_gols'] = gols_
print('-:-'*20)
print(f'\n{estat_player}')
print('-:-'*20, end="\n")
for k, v in estat_player.items():
    print(f'\n{k} => {v}')
print('-:-'*20, end="\n")
print('\nESTATISTICA:')
print(f'''O jogador {estat_player["nome"]} jogou
{estat_player["num_jogos"]} partidas e fez:''', end=None)
for jg, g in enumerate(estat_player['gols']):
    print(f'Na partida {jg+1} fez {g} gols')
