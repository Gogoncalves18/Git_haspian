# Crie um programa que tenha 4 jogadores em um dict e
# todos joguem numeros aleatorios
# depois ordene este dict do maior numero para o menor

import random
from operator import itemgetter
# funcao para ordenar um
# dicionario, porem ele
# transforma o resultado
# em lista e é usada dentro
# do sorted
players = {
            'jogador_1': random.randint(1, 6),
            'jogador_2': random.randint(1, 6),
            'jogador_3': random.randint(1, 6),
            'jogador_4': random.randint(1, 6),
        }
for k, v in players.items():  # Rodo todos os items lendo K e V
    print(f'{k} jogou o numero {v}')
print('-*-'*15)
rank = []
# Abaixo a funcao dentro do sorted para usar o itemgetter com pos (1)
# ao qual pega o segundo elemento e ordena por ele, com a
# possibilidade de usar o reverse
rank = sorted(players.items(), key=itemgetter(1), reverse=True)
for pos, i in enumerate(rank):
    # Como resultado tenho uma lista
    # ao qual posso printar os resultados
    # fazendo interacoes sobre ela
    print(f'\nO {pos+1}˙ colocado foi {i[0]} com {i[1]} pontos.')
