'''Programa para apresentar de fora interativa o sistema de help
através de função. A saida da função precisa usar cores para distinuir
titulo, conteúdo e fim de programa que será finalizando com o usuario
digitando S'''

cores = ('\033[m',          # 0 = Sem Cor
         '\033[1;30;41m',   # 1 = Vermelho
         '\033[1;30;42m',   # 2 = verde
         '\033[1;30;43m',   # 3 = amarelo
         '\033[1;30;44m',   # 4 = azul
         '\033[1;30;45m',   # 5 = roxo
         '\033[7;30m',      # 6 = branco
         )

cores2 = ('\033[m',          # 0 = Sem Cor
          '\033[0;31;40m',   # 1 = Vermelho
          '\033[0;32;40m',   # 2 = verde
          '\033[0;33;40m',   # 3 = amarelo
          '\033[0;34;40m',   # 4 = azul
          '\033[0;35;40m',   # 5 = roxo
          '\033[7;30m',      # 6 = branco
          )


def titulo(msg, cor=0):
    """
    ->Função para trocar a cor de fundo das saídas de texto ou comando.
      Função já possui metodo Print!
    :param cor: definição de cor, 0 é sem cor
    :param cor=1: Vermelho
    :param cor=2: Verde
    :param cor=3: Amarelo
    :param cor=4: Azul
    :param cor=5: Roxo
    :param cor=6: Branco
    """


# Programa principal
    tam = len(msg)+(60-len(msg))
    print(cores[cor])
    print('-'*tam)
    print(f'{msg:^{tam}}')
    print('-' * tam, end='')
    print(cores[0], end='')
    print('')


def texto(msg, cor=0):
    """
    ->Função para trocar a cor do texto ou comando.
      Função possui método Return!
    :param cor: definição de cor, 0 é sem cor
    :param cor=1: Vermelho
    :param cor=2: Verde
    :param cor=3: Amarelo
    :param cor=4: Azul
    :param cor=5: Roxo
    :param cor=6: Branco
    """

# Programa principal
    return f'{cores2[cor]}{msg}{cores2[0]}'
