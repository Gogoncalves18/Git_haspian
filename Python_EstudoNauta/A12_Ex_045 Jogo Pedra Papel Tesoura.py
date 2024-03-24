from random import randint  # importacao modulo para sortear o numero do
# computador
import time  # importacao do modulo para rodar a palavra JOKENPO aos poucos

inic_play = True
while inic_play:  # Looping para manter o jogo rodando ate
    # que o jogador nao queira mais. S para continuar e N para sair.'''
    print('\n{:<20} \033[1;31;41m{:^25}\033[m {:>20}'
          .format('-_-'*15, 'INICIANDO JOGO', '-_-'*15))
    print('''Escolha sua opcao:
    \n
    [1] PEDRA
    [2] PAPEL
    [3] TESOURA
    ''')
    num_player = int(input('Qual a sua jogada? '))
    num_comp = randint(1, 3)  # range de sorteio para computador
    # criacao de um ID para a escolha do computador junto com o
    # descritivo da jogada
    if num_comp == 1:
        id_comp = 'PEDRA'
    elif num_comp == 2:
        id_comp = 'PAPEL'
    else:
        id_comp = 'TESOURA'
    # Abaixo ocorre 3 testes para comparar o player e computador
    # e decidir o vencedor
    if num_player == 1:
        time.sleep(1)
        print('\nJO...')
        time.sleep(1)
        print('\nKEN...')
        time.sleep(1)
        print('\nPO!!!!')
        print('\n{}'.format('-_-'*30))
        print('\nA JOGADA DO COMPUTADOR FOi \033[1;33;42m{:^10}\033[m'
              .format(id_comp))
        print('\nSUA JOGADA FOi \033[1;33;42m{:^10}\033[m'.format('PEDRA'))
        print('\n{}'.format('-_-'*30))
        if num_comp == 1:
            print('\n\033[1;33;43m{:^30}\033[m'
                  .format('VOCES EMPATARAM !!!! HAHAHAHAHAHAHH!!!!!'))
        elif num_comp == 2:
            print('\n\033[1;31;41m{:^30}\033[m'
                  .format('VOCE PERDEU !!!! PAPEL COMEU PEDRA!!!!!'))
        else:
            print('\n\033[1;30;42m{:^30}\033[m'
                  .format('VOCE GANHOUUUUU!!! PEDRA QUEBROU TESOURA!!!!!'))
    elif num_player == 2:
        time.sleep(1)
        print('\nJO...')
        time.sleep(1)
        print('\nKEN...')
        time.sleep(1)
        print('\nPO!!!!')
        print('\n{}'.format('-_-'*30))
        print('\nA JOGADA DO COMPUTADOR FOi \033[1;33;42m{:^10}\033[m'
              .format(id_comp))
        print('\nSUA JOGADA FOi \033[1;33;42m{:^10}\033[m'.format('PAPEL'))
        print('\n{}'.format('-_-'*30))
        if num_comp == 1:
            print('\n\033[1;30;42m{:^30}\033[m'
                  .format('VOCE GANHOUUUUU!!! PAPEL COMEU PEDRA!!!!!'))
        elif num_comp == 2:
            print('\n\033[1;33;43m{:^30}\033[m'
                  .format('VOCES EMPATARAM !!!! HAHAHAHAHAHAHH!!!!!'))
        else:
            print('\n\033[1;31;41m{:^30}\033[m'
                  .format('VOCE PERDEU !!!!  TESOURA CORTOU PAPEL!!!!!'))
    elif num_player == 3:
        time.sleep(1)
        print('\nJO...')
        time.sleep(1)
        print('\nKEN...')
        time.sleep(1)
        print('\nPO!!!!')
        print('\n{}'.format('-_-'*30))
        print('\nA JOGADA DO COMPUTADOR FOi \033[1;33;42m{:^10}\033[m'
              .format(id_comp))
        print('\nSUA JOGADA FOi \033[1;33;42m{:^10}\033[m'.format('TESOURA'))
        print('\n{}'.format('-_-'*30))
        if num_comp == 1:
            print('\n\033[1;31;41m{:^30}\033[m'
                  .format('VOCE PERDEU !!! PEDRA QUEBRA TESOURA!!!!!'))
        elif num_comp == 2:
            print('\n\033[1;30;42m{:^30}\033[m'
                  .format('VOCE GANHOUUUUU !!!! TESOURA CORTOU PAPEL!!!!!'))
        else:
            print('\n\033[1;33;43m{:^30}\033[m'
                  .format('VOCES EMPATARAM !!!! HAHAHAHAHAHAHH!!!!!'))
    # Teste para validar a entrada de teclado para respnder sobre continuacao
    # do jogo
    while True:
        resp_saida = str(input('''\nVamos tentar a SORTE novamente?
        Pressione "S" para tentar novamente.
        Pressione "N" para sair do jogo.
        ''')).upper()[0]
        if resp_saida == 'S' or resp_saida == 'N':
            break
        elif resp_saida != 'S' or 'N':
            print('LETRA ERRA!')
# Ultimo teste de While para fechar ou continuar o looping do jogo.
    if resp_saida == 'n' or resp_saida == 'N':
        inic_play = False
    else:
        inic_play = True
print('\n{:<20} \033[1;31;41m{:^25}\033[m {:>20}'
      .format('-_-'*15, 'FIM DO JOGO', '-_-'*15))
