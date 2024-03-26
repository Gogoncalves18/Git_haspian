# Tabela ASC para padrao de cores para ser utiliza na saida do terminal
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
# Fim do padrao de cores

# Funcao para ser chamada em titulos e texto para uso da tabela acima


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


# Programa principal da FUNCAO
    tam = len(msg)+(76-len(msg))
    print(cores[cor])
    print('-'*tam)
    print(f'{msg:^{tam}}')
    print('-' * tam)
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

# Programa principal da FUNCAO
    return f'{cores2[cor]}{msg}{cores2[0]}'


# PROGRAMA PRINCIPAL PARA QUESTAO 2

titulo('Bem vindo a Loja de Cupuaçu e Açai do Gustavo de Oliveira\
 Gonçalves', 2)  # Definicao de titulo de boas vindas
titulo('CARDÁPIO', 3)
# Valores de produto para facil manutencao
vlrs_prod = {'CP': [9, 14, 18], 'AC': [11, 16, 20]}

tam = 76  # Tamanho maximo para tabulacao, cuida tamanho de tela
sobra = int(((tam-40)/2))  # Divisao para preenchimento de linha
# Inicia do tratamento da tabulacao
print('-' * sobra, end=' ')
print('| Tamanho | Cupuaçu (CP) | Açai (AC) |', end=' ')
print('-' * sobra)
print('-' * sobra, end=' ')
print('|    P    |   R$  9,00   | R$ 11,00  |', end=' ')
print('-' * sobra)
print('-' * sobra, end=' ')
print('|    M    |   R$ 14,00   | R$ 16,00  |', end=' ')
print('-' * sobra)
print('-' * sobra, end=' ')
print('|    G    |   R$ 18,00   | R$ 20,00  |', end=' ')
print('-' * sobra)
print('-' * tam)
# Fim da tabulacao

pedido = {}  # Recebe o pedido por produto, dados temporarios
pedidos = []  # Recebe o aculamento do pedido de varios items

while True:  # Loop para inserir varios itens
    while True:  # Loop para validar entrada do sabor
        resp_sabor = str(input('''Qual sabor você deseja:
                    Digite [ CP ] para Cupuaçu!
                    Digite [ AC ] para Açaí
                    Resposta do Usuário: '''
                               ).upper())
        if resp_sabor == 'CP' or resp_sabor == 'AC':
            pedido["prod"] = resp_sabor
            break
        else:
            print(texto('\nSabor INVÁLIDO, digitar CP ou AC!!!', 1), '\n')

    while True:  # Loop para validar entrada do tamanho
        resp_tam = str(input('''Qual tamanho (P/M/G):
                    Resposta do Usuário: '''
                             ).upper())
        if resp_tam in 'PMG':
            pedido["tam"] = resp_tam
            break
        else:
            print(texto('\nTamanho INVÁLIDO, digitar (P/M/G)!!!', 1), '\n')
    # Copia dos dados do pedido para dentro da lista pedidos
    pedidos.append(pedido.copy())
    ped_added = input('\nVocê deseja adicionar mais um pedido? [S]\
 ou [N]: ').upper()
    # Validacao da resposta de encerramento do pedido
    while ped_added not in 'SN':
        ped_added = input('\nDigite apenas "S" ou "N" para mais\
 pedido: ').upper()
        if ped_added in 'SN':
            break
    if ped_added == 'S':
        continue
    elif ped_added == 'N':
        break
# Acumulador do valor dos pedidos
vlr_total = 0
titulo('\nO resumo de seu PEDIDO:', 3)  # Titulo que puxa tabela de cores
# Laco para coletar os pedidos na lista de pedidos e calcular o vlr total
for i in pedidos:
    if i['tam'] == 'P':
        t = 0
    elif i['tam'] == 'M':
        t = 1
    else:
        t = 2
    vlr_total += vlrs_prod[i['prod']][t]
    print(f'1x ----- {i['prod']} no valor de R${vlrs_prod[i['prod']][t]:.2f}')

# Encerramento do pedido com o valor total
print(texto(f'\nO valor total de seu pedido: R${vlr_total:.2f}', 2), '\n')
