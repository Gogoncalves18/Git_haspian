'''Programa para apresentar de fora interativa o sistema de help
 através de função. A saida da função precisa usar cores para
 distinuir titulo, conteúdo e fim de programa que será finalizando
com o usuario digitando S'''

cores = ('\033[m',          # 0 = Sem Cor
         '\033[0;30;41m',   # 1 = Vermelho
         '\033[0;30;42m',   # 2 = verde
         '\033[0;30;43m',   # 3 = amarelo
         '\033[0;30;44m',   # 4 = azul
         '\033[0;30;45m',   # 5 = roxo
         '\033[7;30m',      # 6 = branco
         )


def comand(cmd):
    titulo(f'\nAcessando o manual do comando {cmd}', 4)
    print(cores[6], end='')
    help(cmd)
    print(cores[0], end='')


def titulo(msg, cor=0):
    """
    ->Função para trocar a cor de fundo das saídas de texto ou comando.
    :param cor: definição de cor, 0 é sem cor
    :param cor=1: Vermelho
    :param cor=2: Verde
    :param cor=3: Amarelo
    :param cor=4: Azul
    :param cor=5: Roxo
    :param cor=6: Branco
    """
    tam = len(msg)+6
    print(cores[cor])
    print('-'*tam)
    print(f'{msg:^{tam}}')
    print('-' * tam, end='')
    print(cores[0])


# Programa principal:
while True:
    titulo('Analise de comando Python através do Help', 2)
    resp = str(input('\nDigite metodo para ver o help ou [S]\
 para sair: '))
    if resp.upper() == 'S':
        break
    else:
        comand(resp)
titulo('Programa encerrado', 1)
