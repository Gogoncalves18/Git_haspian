from dotenv import load_dotenv
from os import getenv
import os


load_dotenv()
# Dict para armazenar por linha os resultados da combinacao
res = {}
# Numero de combinacoes por linha
comb = 5
# Qtd de numeros para o jogo
lim = 100
# Lista de numero para combinacao
lst_num = []
# Nomes para coluna do DF
coluns = []
# Numeros por linha do jogo para ser combinado
linJ = {}

# Qtd de colunas no jogo
col = 5
# Criacao de lista que formara coluna dos resultados
for c in range(1, col+1):
    coluns.append('Col_' + str(c))
coluns.append('LinJ')

# Criacao da lista
cont = 1
linha = 0
for i in range(1, lim+2):
    if cont < 11:
        cont += 1
        lst_num.append(i)
    elif cont > 10:
        linha += 1
        cont = 2
        linJ[linha] = lst_num
        lst_num = []
        lst_num.append(i)
# print(linJ)
# Padrao de onde sera salvo arquivo
table = getenv("loc_name_xls")
path_txt = getenv("path_res_txt")
txt = getenv("name_txt")
path_complete_txt = os.path.join(path_txt, txt)


def conf_existe(arq):
    try:
        with open(arq) as arq_res:
            if arq_res:
                return True
    except FileNotFoundError:
        return False


def combinar_jogo(lista_nums, qtd_num_a_comb):
    # combinar_jogo('ABCD', 2) → AB AC AD BC BD CD
    # combinar_jogo(range(4), 3) → 012 013 023 123

    lista_jogo = tuple(lista_nums)
    n = len(lista_jogo)
    if qtd_num_a_comb > n:
        # finaliza o jogo
        return
    posicoes = list(range(qtd_num_a_comb))

    yield tuple(lista_jogo[i] for i in posicoes)
    while True:
        for i in reversed(range(qtd_num_a_comb)):
            if posicoes[i] != i + n - qtd_num_a_comb:
                break
        else:
            return
        posicoes[i] += 1
        for j in range(i+1, qtd_num_a_comb):
            posicoes[j] = posicoes[j-1] + 1
        yield tuple(lista_jogo[i] for i in posicoes)


# Grupo de linhas para validacao
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Zeramento do contador linhas
lin1 = 0
lin2 = 0
lin3 = 0
lin4 = 0
lin5 = 0
lin6 = 0
lin7 = 0
lin8 = 0
lin9 = 0
lin10 = 0
# Zeramento do contador linhas par impar da linha 1 e 2
lin1_par = 0
lin1_impar = 0
lin2_par = 0
lin2_impar = 0
lin3_par = 0
lin3_impar = 0
lin4_par = 0
lin4_impar = 0
lin5_par = 0
lin5_impar = 0
lin6_par = 0
lin6_impar = 0
lin7_par = 0
lin7_impar = 0
lin8_par = 0
lin8_impar = 0
lin9_par = 0
lin9_impar = 0
lin10_par = 0
lin10_impar = 0

# Funcao para combinacao
jogo = combinar_jogo(range(1, 21), 10)
# numero de jogadas validas
possib = 0
resultado = 0
# Variavel de comparacao para controle da sequencia
v = None
v2 = None
# Quantidade de sequencias existentes no jogo
qtd_rep = 0
# Definicao se ha ou nao sequencia
possui_seq = False
# Valor "qtd_de_seq = 1" para 1 sequencia ou 2 numeros em sequencia
qtd_de_seq = 4

# cada jodada trara uma sequencia de resultados dentro dos criterios
for jogada in jogo:
    for i in jogada:
        for k, v in linJ.items():
            if i in v:
                if i % 2 == 0:
                    if k == 1:
                        lin1 += 1
                        lin1_par += 1
                    elif k == 2:
                        lin2 += 1
                        lin2_par += 1
                    elif k == 3:
                        lin3 += 1
                        lin3_par += 1
                    elif k == 4:
                        lin4 += 1
                        lin4_par += 1
                    elif k == 5:
                        lin5 += 1
                        lin5_par += 1
                    elif k == 6:
                        lin6 += 1
                        lin6_par += 1
                    elif k == 7:
                        lin7 += 1
                        lin7_par += 1
                    elif k == 8:
                        lin8 += 1
                        lin8_par += 1
                    elif k == 9:
                        lin9 += 1
                        lin9_par += 1
                    elif k == 10:
                        lin10 += 1
                        lin10_par += 1
                else:
                    if k == 1:
                        lin1 += 1
                        lin1_impar += 1
                    elif k == 2:
                        lin2 += 1
                        lin2_impar += 1
                    elif k == 3:
                        lin3 += 1
                        lin3_impar += 1
                    elif k == 4:
                        lin4 += 1
                        lin4_impar += 1
                    elif k == 5:
                        lin5 += 1
                        lin5_impar += 1
                    elif k == 6:
                        lin6 += 1
                        lin6_impar += 1
                    elif k == 7:
                        lin7 += 1
                        lin7_impar += 1
                    elif k == 8:
                        lin8 += 1
                        lin8_impar += 1
                    elif k == 9:
                        lin9 += 1
                        lin9_impar += 1
                    elif k == 10:
                        lin10 += 1
                        lin10_impar += 1
# #   PAREI AQUI
    # Valida se nao ultrapassou a contagem de numeros por linha
    if lin1 < 6 and lin2 < 6 and lin3 < 6 and lin4 < 6\
       and lin5 < 6 and lin6 < 6 and lin7 < 6 and lin8 < 6\
       and lin9 < 6 and lin10 < 6:

        # Valida a contagem de par e impar aceito por linha
        if lin1_par < 6 and lin1_impar < 6 and lin2_par < 6 and lin2_impar < 6:

            # Validacao do jogo - Procura se ha sequencias dentro da jogada
            # combinada. Info e cada numero dentro da jogada
            for info in jogada:
                # Contador da variavel comeca vazio no primeiro numero
                if v is None:
                    v = info
                else:
                    v = info
                if v == v2:
                    v2 = v + 1
                    qtd_rep += 1

                    # Valor para 1 sequencia ou 2 numeros em sequencia
                    if qtd_rep >= qtd_de_seq:
                        possui_seq = True
                else:
                    # print('OK')
                    v2 = v + 1
                    if possui_seq is False:

                        # Valor para 1 sequencia ou 2 numeros em sequencia
                        if qtd_rep >= qtd_de_seq:
                            possui_seq = True
                        qtd_rep = 0
            if possui_seq is True:
                possib += 1
                # print(f'JOGO {possib} com 4 SEQUENCIA => {jogada}')
            else:
                resultado += 1
                possib += 1
                # Apresentacao do resultado valido, aqui deve entrar a
                # exportacao dos numeros
                print(f'Resultado ({resultado} - JOGADA {possib} <<'
                      f' >> {jogada}')
                if conf_existe(path_complete_txt) is False:
                    with open(path_complete_txt, 'w') as arq_res:
                        arq_res.write(f'Resultado ({resultado} - '
                                      f'JOGADA {possib} << >> {jogada}\n')
                else:
                    with open(path_complete_txt, 'a') as arq_res:
                        arq_res.write(f'Resultado ({resultado} - '
                                      f'JOGADA {possib} << >> {jogada}\n')
        else:
            possib += 1
            # print(f'JOGO {possib} Impar/Par falhou => {jogada}')
    else:
        possib += 1
        # print(f'JOGO {possib} FORA Lin1 ou Lin2 => {jogada}')

    # Zeramento do contador linhas
    lin1 = 0
    lin2 = 0
    lin3 = 0
    lin4 = 0
    lin5 = 0
    lin6 = 0
    lin7 = 0
    lin8 = 0
    lin9 = 0
    lin10 = 0
    # Zeramento do contador linhas par impar da linha 1 e 2
    lin1_par = 0
    lin1_impar = 0
    lin2_par = 0
    lin2_impar = 0
    lin3_par = 0
    lin3_impar = 0
    lin4_par = 0
    lin4_impar = 0
    lin5_par = 0
    lin5_impar = 0
    lin6_par = 0
    lin6_impar = 0
    lin7_par = 0
    lin7_impar = 0
    lin8_par = 0
    lin8_impar = 0
    lin9_par = 0
    lin9_impar = 0
    lin10_par = 0
    lin10_impar = 0
    qtd_rep = 0
    possui_seq = False
