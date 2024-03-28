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


# Funcao escolha_servico
def escolha_servico():
    """
    Função para escolha de serviço através de um código alfa e com
    regras de digitaçao para validação da entrada de dados
    """

# Programa da função escolha_servico
    while True:  # Validacao de dados de entrada
        resp_user = input('\nCódigo do serviço desejado: ').upper()
        if resp_user == 'DIG':
            return resp_user
        elif resp_user == 'ICO':
            return resp_user
        elif resp_user == 'IBO':
            return resp_user
        elif resp_user == 'FOT':
            return resp_user
        else:
            print(texto('\nDIGITE UM CODÍGO VÁLIDO!', 1), '\n')
            continue


# Funcao num_pagina
def num_pagina(cod):
    """
    Função para perguntar número de páginas e devolver este valor
    com os descontos. Há uma validação de entrada de dados na função
    """


# Programa da função num_pagina
    while True:  # Validacao de daados de entrada
        # Variavel para manutencao dos vlrs de servico
        vlrs_prod = {'DIG': 1.10, 'ICO': 1, 'IBO': 0.40, 'FOT': 0.20}
        try:  # Validacao de input numerico inteiro
            n_pag = int(input('Quantas páginas vc deseja? '))
        except ValueError:
            print(texto('\nDigite apenas um número inteiro!', 1))
            continue
        else:  # Aplicacao da regra de desconto com retorno de pagina
            # e valor total das paginas com desconto
            if n_pag < 20:
                vlr_pgs = n_pag * vlrs_prod[cod]
                return (n_pag, vlr_pgs)
            elif n_pag >= 20 and n_pag < 200:
                vlr_pgs = (n_pag * vlrs_prod[cod]) * 0.85
                return (n_pag, vlr_pgs)
            elif n_pag >= 200 and n_pag < 2000:
                vlr_pgs = (n_pag * vlrs_prod[cod]) * 0.80
                return (n_pag, vlr_pgs)
            elif n_pag >= 2000 and n_pag < 20000:
                vlr_pgs = (n_pag * vlrs_prod[cod]) * 0.75
                return (n_pag, vlr_pgs)
            elif n_pag >= 20000:
                print(texto('\nNão aceitamos pedidos acima de 20000\
 páginas\n', 3))
                continue


# Funcao servico_extra
def servico_extra():
    """
    Função para perguntar sobre a adição de mais dois tipos de serviços
    após a escolha do produto/serviço anterior
    """


# Programa da função servico_extra
    while True:  # Validacao de entrada de dados
        vlr_x = float()  # Variavel para receber o vlr servico escolhido
        # Validacao daa escolha do servico extra
        serv_plus = input('\nVocê deseja o serviço de\
 encardenação? [S] ou [N]: ').upper()
        if serv_plus not in 'SN':
            print(texto('\nDigite apenas S ou N', 1))
            continue
        elif serv_plus == 'N':
            break
        else:
            print(texto('''\nOpções disponíveis:
                        1 - Encardenação Simples - R$15,00
                        2 - Encardenação capa dura - R$40,00
                        0 - Não desejo o serviço extra''', 6))
            while True:  # Tela de entrada do servico extra
                try:  # Validacao de entrada do serv extra
                    option = int(input('\nDigite a opção acima: '))
                except ValueError:
                    print(texto('\nDigite uma opção válida!', 1))
                else:
                    if option == 1:
                        vlr_x = 15.00
                        return vlr_x
                    elif option == 2:
                        vlr_x = 40.00
                        return vlr_x
                    elif option == 0:
                        vlr_x = 0.00
                        return vlr_x
                    else:
                        print(texto('\nDigite uma opção válida!', 1))
                        continue
        break


# PROGRAMA PRINCIPAL PARA QUESTAO 3
# Tela de boas vindas com nome
titulo('Bem vindo a Loja SUACOPIA do Gustavo de Oliveira\
 Gonçalves', 2)  # Definicao de titulo de boas vindas

# Apresentacao das opcoes, aparecerá apenas 1x
print(texto('''
Digite o CÓDIGO para o serviço desejado:
        CÓDIGO         Serviço
          DIG  ----- Digitalização
          ICO  ----- Impressão Colorida
          IBO  ----- Impressão Preto e Branco
          FOT  ----- Fotocópia
''', 3))
# Chamada e retorno do servico a escolher, este servira de input para
# a proxima funcao
user_opt_serv = escolha_servico()
# De acordo com o servico escolhido, segue a entrada para calculo
# dos valores,  retorno é uma tupla com nº pagina na posica [0] e
# valor total com desconto na posicao [1]
res_escolha_pag_vlr = num_pagina(user_opt_serv)
# Desmembramento dos valores da tupla para facilitar na apresentacao
# dos resultados
n_pg = res_escolha_pag_vlr[0]
vlr_t_pg = res_escolha_pag_vlr[1]
# Acionamento da validacao de servico extra com retorno de valores de
# acordo com a escolha do usuario
vlr_serv_x = servico_extra()

# Apresentação do resultado do pedido de acordo com os inputs do user
print(texto(f'''\nResumo do seu Pedido:
            Valor Total: R${(vlr_t_pg + vlr_serv_x):.2f}
                (COD de Serviço Escolhido => {user_opt_serv})
                (Nº de páginas => {n_pg})
                (Valor serviço Extra => R${vlr_serv_x:.2f})''', 2))
