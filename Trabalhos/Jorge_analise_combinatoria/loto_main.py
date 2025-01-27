from combinacoes import combinar
from combinacoes import conf_existe
from valida_par_impar import validar_par_impar
from valida_sequencia import validar_sequencia
from valida_coluna import validar_coluna
from valida_diagonal_direita import validar_diagonal_direita
from valida_diagonal_esquerda import validar_diagonal_esquerda
from dotenv import load_dotenv
from os import getenv
import os

load_dotenv()
table = getenv("loc_name_xls")
path_txt = getenv("path_res_txt")
txt = getenv("name_txt")
path_complete_txt = os.path.join(path_txt, txt)

'''VARIAVEIS'''
# Numero de combinacoes por linha <<<<<<<<<<<<<<<
#comb = 5  # <<<<<<<<<<<<<<
max_seq_diagonal = 5  # <<<<<<<<<<<<<<
qtd_num_por_resultado = 50 # <<<<<<<<
num_inicial_para_combinar = 1 # <<<<<<<<
num_final_para_combinar = 101 # <<<<<<<<
# Valor "qtd_de_seq = 1" para 1 sequencia ou 2 numeros em sequencia
qtd_de_seq = 4  # <<<<<<<<<<<<<<
# Controle de numero de colunas aceitas
qtd_coluna_por_res = 5  # <<<<<<<<<<<<<<

# Dict para armazenar por linha os resultados da combinacao
res = {}
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

# numero de jogadas validas
possib = 0
lin = 0
# Funcao para combinacao
# jogadas = [(1, 2, 3, 5, 7, 11, 16, 18, 19, 20, 23, 24, 26, 27, 29, 32, 34, 37, 38, 40, 42, 43, 45, 47, 50, 51, 54, 55, 58, 59, 61, 62, 63, 68, 69, 71, 74, 75, 76, 80, 82, 84, 86, 87, 88, 93, 95, 96, 99, 100)]

for jogo in combinar(range(num_inicial_para_combinar, num_final_para_combinar), qtd_num_por_resultado):
    # for jogo in jogadas:
    lin += 1
    possib += 1
    validacao_par_impar_seq = validar_par_impar(jogo, linJ, possib)
    if validacao_par_impar_seq == 0:
        pass
    else:
        validacao_sequencia = validar_sequencia(validacao_par_impar_seq, qtd_de_seq, possib)
        if validacao_sequencia == 0:
            pass
        else:
            validacao_coluna = validar_coluna(validacao_sequencia, qtd_coluna_por_res, possib, linJ)
            if validacao_coluna == 0:
                pass
            else:

                jogada_validada_D = validar_diagonal_direita(validacao_coluna, max_seq_diagonal)
                jogada_validada_E = validar_diagonal_esquerda(validacao_coluna, max_seq_diagonal)

                if jogada_validada_D is True and jogada_validada_E is True:
                    # ==> EXPORTACAO DOS DADOS VALIDOS <==
                    if conf_existe(path_complete_txt) is False:
                        with open(path_complete_txt, 'w') as arq_res:
                            arq_res.write(f'{validacao_coluna}\n')
                    else:
                        with open(path_complete_txt, 'a') as arq_res:
                            arq_res.write(f'{validacao_coluna}\n')
                    print(f'Executada linha {lin} - Resultado {validacao_coluna}')