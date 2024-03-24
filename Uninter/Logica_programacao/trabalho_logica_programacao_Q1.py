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
    tam = len(msg)+(80-len(msg))
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

# Programa principal da FUNCAO
    return f'{cores2[cor]}{msg}{cores2[0]}'


# PROGRAMA PRINCIPAL PARA QUESTAO 1

titulo('Bem vindo a Loja do Gustavo de Oliveira Gonçalves -\
       RU: 4566100', 2)  # Definicao de titulo de boas vindas
lst_prod = []  # Lista de produtos inseridos sem limite de qtd
print()
while True:  # Loop para inserir varios produtos com vlr e qtd
    while True:  # Validacao de entrada de dados
        try:  # Validacao para num INT ou FLOAT
            vlr_prod = int(input('Qual valor do produto? : '))
        except Exception:  # as msg_err:
            # print(msg_err.__class__)
            print(texto('\nVlr Produto deve ser inteiro ou com\
 "." para vlr com centavos : ', 1), "\n")
            continue
        else:
            break
    while True:  # Validacao para num INT
        try:
            qtd_prod = int(input('Quantos itens deste produto você\
 deseja? : '))
        except Exception:  # as msg_err:
            # print(msg_err.__class__)
            print(texto('\nQuantidade deve ser inteira: ', 1), "\n")
            continue
        else:
            break
    soma_item = vlr_prod * qtd_prod  # Vlr final do produto x qtd
    lst_prod.append(soma_item)  # Armazenamento dos dados em lista
    add_prod = str(input('\nGostaria de inserir mais algum produto?\
 [S] ou [N] : ')).upper()[0]  # Confirmacao de novos produtos
    if add_prod in 'SN':
        # Validacao da resposta do user para novos produtos
        if add_prod in 'S':  # Joga o loop para inicio, LINHA 71
            # print(f'Mais prod. {add_prod}')
            continue
        elif add_prod in 'N':  # Finaliza a entrada de dados
            # print(f'Acabou {add_prod}')
            break
    else:
        while add_prod not in 'SN':  # Forca o user a entrar com S ou N
            add_prod = str(input('\nDigite apenas "S" para continuar\
 adicioando produtos para OU "N" para finalizar a compra: ')).upper()[0]
# Valor total do pedido formatado com ','
print(texto(f'\nResumo do pedido sem desconto: R${sum(lst_prod):.2f}',
            3).replace('.', ','), "\n")
vlr_final = sum(lst_prod)  # Valor total do pedido
desc = 0
# Validacao de qual desconto sera aplicado no pedido
if vlr_final >= 2500 and vlr_final < 6000:  # Definicao de faixa de vlr
    desc = 0.04  # Desconto para faixa
    vlr_final -= vlr_final*desc
elif vlr_final >= 6000 and vlr_final < 10000:  # Definicao de faixa de vlr
    desc = 0.07  # Desconto para faixa
    vlr_final -= vlr_final*desc
elif vlr_final >= 10000:  # Definicao de faixa de vlr
    desc = 0.11  # Desconto para faixa
    vlr_final -= vlr_final*desc
# Resultado do pedido com desconto
print(texto(f'\nVlr do pedido com DESCONTO: R${vlr_final:.2f}\
 (Desconto de {desc*100:.0f}%)', 2).replace('.', ','), "\n")
