'''Criar um programa que gerencie a estatica de um jogador.
Gerenciar o numero de jogos e gols por jogos e total de gols.
Guardar tudo em um dicionario e posterior apresentar:
-Valor de cada campo
-Numero de partidas
-Gols em cada partida
-Total de gols
-Perguntar de quantos jogadores quiser e montar estatistica deles
'''
estat_player = {}  # Guarda todos os dados
lst_gols = []  # Lista somente para gerar copia para dentro do Dict
gols_ = 0  # variavel para somar gols
cad_players = []
add_player = 's'  # Variavel usada para iniciar e finalizar o programa
while add_player != 'N':
    estat_player.clear()
    estat_player['nome'] = str(input('\nNome do Jogador: ')).title()
    estat_player['num_jogos'] = int(input('\nQdts jogos foram\
registrados: '))
    for n in range(0, estat_player['num_jogos']):
        # Loop sobre o num de jogos dentro do dict
        lst_gols.append(int(input(f'''\nQuantos gols ele fez na partida
                                  {n+1}: ''')))
    estat_player['gols'] = lst_gols.copy()
    # Inseri os gols como lista no campo V de uma K
    lst_gols.clear()
    for g in estat_player['gols']:  # contagem de gols
        gols_ += g
    estat_player['tot_gols'] = gols_
    # Linha abaixo para definicao de final de programa
    add_player = str(input('''\nQuer adicionar mais um jogador?\
                           [S] ou [N]''')).upper()[0]
    while True:
        # Validacao de entrada da reposta permanecer ou sair do
        # programa
        if add_player not in 'SN':
            add_player = str(input('''\nDigite somente: [S] ou
                                   [N]''')).upper()[0]
            continue
        else:
            break
    cad_players.append(estat_player.copy())
    # Cadastra o DICT dos dados do jogador em uma lista
print('-:-'*20)
print(f'\n{cad_players}')
print()
print('-='*30)
print(f'\n{"COD":<10}{"JOGADOR":<10}{"GOLS":<10}{"TOTAL GOLS":<10}')
print('-'*42)
for pos, i in enumerate(cad_players):
    # Rodo os items e posicoes dentro de uma lista
    print(f'{pos:<10}', end='')  # Printo a posicao e trago a proxima
    # linha de baixo para cima com o end=
    for dado in i.items():  # Aqui leio os itens dentro de um DICT
        if dado[0] != 'num_jogos':
            # faco uma validacao de cada item na POS 0 de uma TUPLA pois
            # coverteu os itens em tuplas E faco teste para nao ler a
            # informacao de numero de jogos, pois nao me interessa
            # mostrar ela
            print(f'{str(dado[1]):<10}', end=' ')
            # Apresento os valores da posicao 1 de cada tupla lida
            # precisei converter em STR para usar o string format :<10
print()
print('-'*42)
analys = 0
while True:  # Looping para pedir analise dos jogadores
    print('\nAnalisar qual jogodor? ')
    analys = int(input('Digite o [ID] ou [999] para sair: '))
    if analys == 999:  # Sair do programa
        break
    else:
        # Leio o item de uma lista atraves do ANALYS que me dá um DICT,
        # e no DICT apenas leio o campo que me interessa
        print(f'''O jogador {cad_players[analys]["nome"]} tem
              {cad_players[analys]["num_jogos"]}
jogos com a seguinte performance:''')
        for part, g in enumerate(cad_players[analys]["gols"]):
            # Aqui eu interajo sobre um lista que está em um Value de
            # uma KEY que está em um DICT
            print(f'Na partida {part+1}, ele fez {g} gols.')
            # Apresento os gols em cada valor dentro da lista
