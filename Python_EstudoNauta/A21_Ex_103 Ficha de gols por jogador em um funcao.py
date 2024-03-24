'''Crie um programa que tenha uma funcao chamada ficha(), que receba
dois parametros opcionais: o Nome e o numero de gols e por fim apresente
a ficha do jogador. A entrada de dados pode ser numerica ou string.
'''


def ficha(nome='desconhecido', gols='0'):
    # Defini parametro fixo caso não receba nada
    return (f'\nO jogador {nome}, fez {gols} gols!')


# PROGRAMA PRINCIPAL:

jog = str(input('\nDigite nome do jogador: '))
# Pego o nome do jogador, se foi digitado
gol = str(input('Digite o numero de gols dele: '))
# Pego os gols, se foi digitado
if jog.strip() == '' and gol.isnumeric():
    # Dou um strip para tirar qq espaco e se ele for vazio para o nome
    # jogador e há numero em gols executo o print abaixo, so com gols
    print(ficha(gols=gol))
elif jog.strip() == '' and gol == '':
    # Se o nome do jogador e gol vier vazio, passo para funcao a
    # execução dos parâmetros pre configurados
    print(ficha())
elif len(jog) > 1 and gol == '':
    # Se recebo algo maior que 1 em nome do jogador, é porque
    # escreveram algo e valido se há gol
    print(ficha(nome=jog))
elif len(jog) > 1 and gol.isnumeric():
    # Aqui valido se tem nome escrito e gol escrito
    print(ficha(nome=jog, gols=gol))
